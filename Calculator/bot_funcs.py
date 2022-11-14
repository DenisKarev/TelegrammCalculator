import logging
from bot_consts import OPERATIONSV, MESSAGE_HI, KEYS_M, KEYS_1, KEYS_2, KEYS_C
from logger1 import write_log, logger as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

COMPLEX1, COMPLEX2, TOPMENU, CHOICE1, CHOICE2, INPUTV, INPUTV2, CONTMENU, FIRSTMENU, SECONDMENU, \
    SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT = range(18)

logging.basicConfig(
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
                    # filename='bot_logs.csv'
                    )
logger = logging.getLogger(__name__)


def start(update, context):
    context.user_data.clear()
    markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
    update.message.reply_text(MESSAGE_HI, reply_markup=markup_key)
    logger.info('Пользователь %s Начал работу', update.message.from_user.first_name)
    return TOPMENU


def top_menu(update, context):
    text = update.message.text
    context.user_data['nums'] = 1 if text == 'Вещественные числа' else 2
    logger.info('Пользователь %s выбрал %s', update.message.from_user.first_name, text)
    write_log('\nПользователь выбрал ' + text)
    if context.user_data['nums'] == 1:
        markup1_key = ReplyKeyboardMarkup(KEYS_1, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите арифметическое действие: ', reply_markup=markup1_key, )
        return CHOICE1
    elif context.user_data['nums'] == 2:
        markup1_key = ReplyKeyboardMarkup(KEYS_2, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите арифметическое действие: ', reply_markup=markup1_key, )
        return CHOICE2


def menu_one(update, context):
    text = update.message.text
    context.user_data['operation'] = text
    write_log(" выбрано действие " + text)
    logger.info('Пользователь %s выбрал %s', update.message.from_user.first_name, text)
    if context.user_data['operation'] == 'Квадратный корень':
        context.user_data['n1'] = False
        update.message.reply_text("Введите вещественное число:")
        return INPUTV
    elif context.user_data['operation'] == 'Предыдущее меню':
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(
            f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        return TOPMENU
    else:
        context.user_data['n1'] = False
        update.message.reply_text("Введите первое вещественное число:")
    return INPUTV2


def menu_two(update, context):
    context.user_data['complex2'] = ''
    context.user_data['complex1'] = ''
    text = update.message.text
    context.user_data['operation'] = text
    logger.info('Пользователь %s выбрал %s', update.message.from_user.first_name, context.user_data['operation'])
    # logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, context.user_data['numberv1'])
    if context.user_data['operation'] == 'Предыдущее меню':
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(
            f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        return TOPMENU
    update.message.reply_text("Введите первое комплексное число через пробел")
    write_log(" выбрано действие " + text)
    return COMPLEX1


def inputv_2number(update, context):
    """Parsing a number"""
    number = update.message.text
    if not context.user_data['n1']:
        try:
            context.user_data['numberv1'] = float(number)
        except:
            update.message.reply_text('Непонятно, попробуйте еще раз')
            return INPUTV2
        logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, number)
        write_log("\nПользователь ввел:  " + str(number))
        context.user_data['n1'] = True
        context.user_data['n2'] = False
        update.message.reply_text('Введите второе вещественное число:')
        return INPUTV2
    else:
        try:
            context.user_data['numberv2'] = float(number)
            logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, number)
            write_log("\nПользователь ввел:  " + number)
        except:
            update.message.reply_text('Непонятно, попробуйте еще раз')
            logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, number)
            write_log("\nПользователь ввел:  " + number)
            return INPUTV2
        if (context.user_data['operation']=='Деление' or context.user_data['operation']=='Целочисленное деление'\
                    or context.user_data['operation']=='Деление с остатком') and context.user_data['numberv2'] == 0:
            update.message.reply_text('Вы пытались разделить на ноль. Это невозможно и запрещено!',
                                reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
            logger.warning('Пользователь %s пытался поделить на ноль!', update.message.from_user.first_name)
            write_log("\nПользователь пытался поделить на ноль !!!")
            return CONTMENU
        context.user_data['n2'] = True
        temp = OPERATIONSV[context.user_data['operation']](
            context.user_data['numberv1'], context.user_data['numberv2'])
        logger.info('Пользователь %s. Результат операции: %s', update.message.from_user.first_name, temp)
        update.message.reply_text(f'Результат операции: {temp}',
                                  reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
        write_log("\nРезультат операции: " + str(temp))
        return CONTMENU


def inputv_number(update, context):
    """Parsing a number"""
    number = update.message.text
    try:
        context.user_data['numberv1'] = float(number)
        logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, context.user_data['numberv1'])
        write_log("\nПользователь ввел:  " + number)
    except:
        update.message.reply_text('Непонятно, попробуйте еще раз')
        logger.info('Пользователь %s ввел %s', update.message.from_user.first_name, context.user_data['numberv1'])
        write_log("\nПользователь ввел:  " + number)
        return INPUTV
    if context.user_data['nums'] == 2:
        context.user_data['complex2'] = float(number)
        result_complex(update, context)
        return CONTMENU
    temp = OPERATIONSV[context.user_data['operation']](
        context.user_data['numberv1'])
    update.message.reply_text(f'Результат операции: {temp}',
                              reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
    return CONTMENU


def inputv_complex1(update, context):
    try:
        text = update.message.text.split()
        context.user_data['complex1'] = complex(float(text[0]), float(text[1]))
    except:
        update.message.reply_text('Непонятно, попробуйте еще раз')
        write_log("Ошибка ввода комплексного числа: " + text+';')
        logger.warning('Пользователь %s: Ошибка ввода 1го комплекного числа: %s', update.message.from_user.first_name, text)
        return COMPLEX1
    if context.user_data['operation'] == 'Квадратный корень' and context.user_data['complex1'] != '':
        context.user_data['result'] = context.user_data['complex1'] ** 0.5
        log(context.user_data['complex1'], context.user_data['operation'], context.user_data['result'])
        logger.info('Пользователь %s извлек Квадратный корень %s: %s', update.message.from_user.first_name, context.user_data['complex1'], context.user_data['result'])
        update.message.reply_text(
            f"Квадратный корень из {context.user_data['complex1']} равен {context.user_data['result']}",
            reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
        return CONTMENU
    if context.user_data['operation'] == 'Возведение в спепень':
        update.message.reply_text("Введите степень")
        return INPUTV
    update.message.reply_text("Введите второе комплексное число")
    return COMPLEX2


def inputv_complex2(update, context):
    try:
        text = update.message.text.split()
        context.user_data['complex2'] = complex(float(text[0]), float(text[1]))
        if context.user_data['operation'] == 'Деление' and float(text[0]) == 0 and float(text[1]):
            update.message.reply_text('Нельзя делить на ноль')
            write_log(" попытка делить на 0" +
                      context.user_data['complex1'] + "на" + context.user_data['complex2'])
            logger.warning('Пользователь %s пытался поделить на ноль!', update.message.from_user.first_name)
            return COMPLEX2
    except:
        update.message.reply_text('Непонятно, попробуйте еще раз')
        write_log(', Ошибка ввода 2го комплекного числа введено ' + str(text))
        logger.warning('Пользователь %s: Ошибка ввода 2го комплекного числа: %s', update.message.from_user.first_name, text)
        return COMPLEX2
    result_complex(update, context)
    return CONTMENU


def cont_menu(update, context):
    """Continue or not"""
    text = update.message.text
    logger.info('Пользователь %s нажал: "Еще разок"',
                    update.message.from_user.first_name)
    if text == 'Еще разок':
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(
            f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        write_log('\nЕще разок ')
        return TOPMENU
    elif text == 'Выход':
        update.message.reply_text('ОКи, приходите еще! %))')
        write_log('\nВыход ')
        return ConversationHandler.END
    else:
        logger.warning('Щось пошло не так',
                       update.message.from_user.first_name)
        return  ConversationHandler.END


def cancel(update, context):
    # определяем пользователя
    # user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s нажал отмену",
                update.message.from_user.first_name)
    write_log("Пользователь выбрал отмену")
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def comlex_operation(update, context):
    text = update.message.text
    com1 = context.user_data['complex1']
    com2 = context.user_data['complex2']
    # update.message.reply_text(f"Первое число{com1} второе число{com2} оператор {context.user_data['operation']}")
    operation = context.user_data['operation']
    if com2 != '':
        if operation == 'Cумма':
            context.user_data['result'] = com1 + com2
        elif operation == 'Разность':
            context.user_data['result'] = com1 - com2
        elif operation == 'Умножение':
            context.user_data['result'] = com1 * com2
        elif operation == 'Деление':
            context.user_data['result'] = com1 / com2
        elif operation == 'Целочисленное деление':
            context.user_data['result'] = com1 // com2
        elif operation == 'Деление с остатком':
            context.user_data['result'] = com1 / com2
        elif operation == 'Возведение в спепень':
            context.user_data['result'] = com1 ** com2
    return context.user_data['result']


def result_complex(update, context):
    result = comlex_operation(update, context)
    log(context.user_data['complex1'], context.user_data['operation'],
        result, context.user_data['complex2'])
    logger.info('Пользователь %s %s комплексных чисел: %s и %s Равна %s', update.message.from_user.first_name, context.user_data['operation'],
                context.user_data['complex1'], context.user_data['complex2'], result)
    update.message.reply_text(f" {context.user_data['operation']} комплексных чисел\n{context.user_data['complex1']}\n"
                              f"{context.user_data['complex2']}\nРавна {result}",
                              reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))