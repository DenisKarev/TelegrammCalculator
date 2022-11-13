# from gtoken.gtoken import g_token
import logging
from bot_funcs import (
    start, top_menu, menu_one, menu_two, inputv_number, inputv_2number, cont_menu, inputv_complex1, inputv_complex2,
    COMPLEX1, COMPLEX2, TOPMENU, CHOICE1, CHOICE2, INPUTV, INPUTV2, CONTMENU,
    SECONDMENU, SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT,
    cancel
)

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
g_token = "5502983826:AAHqnDHCxzwFkZeJI08dxeLk0XNniSUrbMY"

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(g_token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            TOPMENU: [MessageHandler(Filters.regex('^(Вещественные числа|Комплексные числа)$'), top_menu)],
            CHOICE1: [MessageHandler(Filters.regex('^(Cумма|Разность|Умножение|Деление|Целочисленное деление|Деление с остатком|Возведение в спепень|Квадратный корень|Предыдущее меню)$'), menu_one)],
            CONTMENU: [MessageHandler(Filters.regex('^(Еще разок|Выход)$'), cont_menu)],
            INPUTV: [MessageHandler(Filters.text & ~Filters.command, inputv_number)],
            INPUTV2: [MessageHandler(Filters.text & ~Filters.command, inputv_2number)],

            CHOICE2: [MessageHandler(Filters.regex('^(Cумма|Разность|Умножение|Деление|Возведение в спепень|Квадратный корень|Предыдущее меню)$'), menu_two)],

            COMPLEX1: [MessageHandler(Filters.text & ~Filters.command, inputv_complex1)],
            COMPLEX2: [MessageHandler(Filters.text & ~Filters.command, inputv_complex2)],

        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    #START, FIRSTMENU, SECONDMENU, SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT = range(11)
    dispatcher.add_handler(conv_handler)
    

    updater.start_polling()
    updater.idle()