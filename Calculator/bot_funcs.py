import logging
from bot_consts import MESSAGE_HI, KEYS_M, KEYS_1, KEYS_2

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


TOPMENU, CHOICE1, CHOICE2, INPUTV,  FIRSTMENU, SECONDMENU, SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT = range(14)

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
    print(text)
    context.user_data['nums'] = 1 if text == 'Вещественные числа' else 2
    print(context.user_data['nums'])
    if context.user_data['nums'] == 1:
        markup1_key = ReplyKeyboardMarkup(KEYS_1, one_time_keyboard=True)
        update.message.reply_text('Выберите арифметическое действие: ', reply_markup=markup1_key,)
        return CHOICE1
    elif context.user_data['nums'] == 2:
        markup1_key = ReplyKeyboardMarkup(KEYS_2, one_time_keyboard=True)
        update.message.reply_text('Выберите арифметическое действие: ', reply_markup=markup1_key,)
        return CHOICE2


def menu_one(update, context):
    text = update.message.text
    print(text)
    context.user_data['operation'] = text
    if context.user_data['operation'] == 'Квадратный корень' or context.user_data['operation'] == 'Предыдущее меню':
        return 12
    else:
        if context.user_data['numberv2'] == None:
            # markup1_key = ReplyKeyboardMarkup(KEYS_1, one_time_keyboard=True)
            update.message.reply_text("Введите вещ. число:", reply_markup=ReplyKeyboardRemove())
            user = update.message.text
            print(user)
            return INPUTV
        else:
            if context.user_data['operation'] == 'Cумма':
                context.user_data['result'] = context.user_data['numberv1']+context.user_data['numberv2']
            elif context.user_data['operation'] == 'Разность':
                context.user_data['result'] = context.user_data['numberv1'] - context.user_data['numberv2']
            elif context.user_data['operation'] == 'Умножение':
                context.user_data['result'] = context.user_data['numberv1'] * context.user_data['numberv2']
            elif context.user_data['operation'] == 'Деление':
                context.user_data['result'] = context.user_data['numberv1'] / context.user_data['numberv2']
            elif context.user_data['operation'] == 'Целочисленное деление':
                context.user_data['result'] = context.user_data['numberv1'] // context.user_data['numberv2']
            elif context.user_data['operation'] == 'Деление с остатком':
                context.user_data['result'] = context.user_data['numberv1'] / context.user_data['numberv2']
            elif context.user_data['operation'] == 'Возведение в спепень':
                context.user_data['result'] = context.user_data['numberv1'] ** context.user_data['numberv2']
            elif context.user_data['operation'] == 'Квадратный корень':
                context.user_data['result'] = context.user_data['numberv1'] ** 0.5
            # elif context.user_data['operation'] == 'Предыдущее меню':
            update.message.reply_text(f"Результат:{context.user_data['result']}", reply_markup=ReplyKeyboardRemove())
            print(context.user_data['result'])
            return TOPMENU



def menu_two(update, context):
    reply_keyboard = [['Cумма', 'Разность', 'Умножение'],
                      ['Деление', 'Целочисленное деление', 'Деление с остатком'],
                      ['Возведение в спепень', 'Квадратный корень'],
                      ['Предыдущее меню']]
    markup1_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выберите арифметическое действие',
        reply_markup=markup1_key,)
    user = update.message.text
    print(user)
    return CHOICE1


def inputv_number(update, context):
    """Parsing a number"""
    text = update.message.text
    try:
        context.user_data['number1'] = int(text)
    except:
        update.message.reply_text(
        'Not a number!!!',
        reply_markup=ReplyKeyboardRemove)
        return INPUTV
    print('Number !!!!')
    return

def inputv_number2(update, context):
    """Parsing a number"""
    text = update.message.text
    try:
        context.user_data['numberv2'] = int(text)
    except:
        update.message.reply_text(
        'Not a number!!!',
        reply_markup=ReplyKeyboardRemove)
        return INPUTV
    print('Number !!!!')
    return
    

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def modules_menu(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def input_first_num(update, context):
    update.message.reply_text(
        'Введите первое число')
    user = update.message.from_user
    update.message.reply_text(user)
    print(user)
    print(type(user))
    return -1


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
