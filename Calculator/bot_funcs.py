import logging
from bot_consts import OPERATIONSV, MESSAGE_HI, KEYS_M, KEYS_1, KEYS_2, KEYS_C

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
    # print(context.user_data)
    context.user_data.clear()
    # reply_keyboard = KEYS_M
    markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
    update.message.reply_text(MESSAGE_HI, reply_markup=markup_key)
    return TOPMENU


# def restart(update, context):
#     # print(context.user_data)
#     context.user_data.clear()
#     # reply_keyboard = KEYS_M
#     markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
#     update.message.reply_text('', reply_markup=markup_key)
#     return TOPMENU

def top_menu(update, context):
    text = update.message.text
    context.user_data['complex2'] = ''
    context.user_data['complex1'] = ''
    print(text)
    context.user_data['nums'] = 1 if text == 'Вещественные числа' else 2
    print(context.user_data['nums'])
    if context.user_data['nums'] == 1:
        markup1_key = ReplyKeyboardMarkup(KEYS_1, one_time_keyboard=True)
        update.message.reply_text('Выберите арифметическое действие: ', reply_markup=markup1_key, )
        return CHOICE1
    elif context.user_data['nums'] == 2:
        markup1_key = ReplyKeyboardMarkup(KEYS_2, one_time_keyboard=True)
        update.message.reply_text('Выберите арифметическое действие: ', reply_markup=markup1_key, )
        return CHOICE2


def menu_one(update, context):
    text = update.message.text
    print('menu_one', text)
    context.user_data['operation'] = text
    if context.user_data['operation'] == 'Квадратный корень':
        context.user_data['n1'] = False
        update.message.reply_text("Введите вещественное число:")
        user = update.message.text
        return INPUTV
    elif context.user_data['operation'] == 'Предыдущее меню':
        print(context.user_data['operation'])
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        return TOPMENU
    else:
        context.user_data['n1'] = False
        update.message.reply_text("Введите первое вещественное число:")
    user = update.message.text
    print(user)
    return INPUTV2


def menu_two(update, context):
    text = update.message.text
    print(text)
    context.user_data['operation'] = text
    if context.user_data['operation'] == 'Предыдущее меню':
        print(context.user_data['operation'])
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        return TOPMENU
    update.message.reply_text("Введите первое комплексное число через пробел")
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
        context.user_data['n1'] = True
        context.user_data['n2'] = False
        update.message.reply_text('Введите второе вещественное число:')
        print(context.user_data['numberv1'])
        return INPUTV2
    else:
        try:
            context.user_data['numberv2'] = float(number)
        except:
            update.message.reply_text('Непонятно, попробуйте еще раз')
            return INPUTV2
        context.user_data['n2'] = True
        print(context.user_data['numberv2'])
        print(context.user_data['operation'])
        temp = OPERATIONSV[context.user_data['operation']](context.user_data['numberv1'], context.user_data['numberv2'])
        update.message.reply_text(f'Результат операции: {temp}',
                                    reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
        return CONTMENU


def inputv_number(update, context):
    """Parsing a number"""
    number = update.message.text
    try:
        context.user_data['numberv1'] = float(number)
    except:
        update.message.reply_text('Непонятно, попробуйте еще раз')
        return INPUTV
    temp = OPERATIONSV[context.user_data['operation']](context.user_data['numberv1'])
    update.message.reply_text(f'Результат операции: {temp}',
                                reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
    return CONTMENU


def inputv_complex1(update, context):
    """Parsing a number"""
    print("complex1_start")
    try:
        text = update.message.text.split()
        context.user_data['complex1'] = complex(float(text[0]), float(text[1]))
    except:
        update.message.reply_text(
            'Not a Complex number !!!',
            reply_markup=ReplyKeyboardRemove)
        return COMPLEX1
    print('Complex_Number1 !!!!')
    if context.user_data['operation'] == 'Квадратный корень' and context.user_data['complex1'] != '':
         context.user_data['result'] = context.user_data['complex1'] ** 0.5
         update.message.reply_text(
             f"Квадрат корень ! из {context.user_data['complex1']} равен {context.user_data['result']}",
                                reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
         return CONTMENU
    update.message.reply_text("Ведите второе комплексное число")
    return COMPLEX2


def inputv_complex2(update, context):
    """Parsing a number"""
    print("complex2_start")
    try:
        text = update.message.text.split()
        context.user_data['complex2'] = complex(float(text[0]), float(text[1]))
    except:
        update.message.reply_text(
            'Not a Complexnumber !!!',
            reply_markup=ReplyKeyboardRemove)
        return COMPLEX2
    print('Complex2_Number !!!!')
    result = comlex_operation(update, context)
    update.message.reply_text(f" {context.user_data['operation']} комплексных чисел\n{context.user_data['complex1']}\n"
                              f"{context.user_data['complex2']}\nРавна {result}",
                                reply_markup=ReplyKeyboardMarkup(KEYS_C, one_time_keyboard=True))
    # update.message.reply_text(f"давай еще разок")
    return CONTMENU



def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def cont_menu(update, context):
    """Continue or not"""
    text = update.message.text
    if text == 'Еще разок':
        markup_key = ReplyKeyboardMarkup(KEYS_M, one_time_keyboard=True)
        update.message.reply_text(f'Главное меню!\n{MESSAGE_HI[66:]}', reply_markup=markup_key)
        return TOPMENU
    elif text == 'Выход':
        update.message.reply_text('ОКи, приходите еще! %))')
        return ConversationHandler.END
    else:
        logger.warning('Щось пошло не так')


def cancel(update, context):
    # определяем пользователя
    # user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s нажал отмену",
                update.message.from_user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться',
        reply_markup=ReplyKeyboardRemove()
    )
    print(context.user_data)
    return ConversationHandler.END


def comlex_operation(update, context):
    text = update.message.text
    com1 = context.user_data['complex1']
    com2 = context.user_data['complex2']
    print(text)
    update.message.reply_text(f"Первое число{com1} второе число{com2} оператор {context.user_data['operation']}")
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