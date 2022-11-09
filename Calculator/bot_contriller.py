import logging
from bot_funcs import (
    start, top_menu, menu_one, menu_two, inputv_number, cancel,
    TOPMENU, CHOICE1, CHOICE2, INPUTV, FIRSTMENU, SECONDMENU, SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT
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
            CHOICE1: [MessageHandler(Filters.regex('^(Cумма|Разность|Умножение|\
                                                  Деление|Целочисленное деление|Деление с остатком|\
                                                  Возведение в спепень|Квадратный корень|\
                                                  Предыдущее меню)$'), menu_one)],
            CHOICE2: [MessageHandler(Filters.regex('^(Вещественные числа|Комплексные числа)$'), menu_two)],
            # FIRSTMENU: [MessageHandler(Filters.regex('^(Cумма|Разность|Умножение|\
            #                                         Деление|Целочисленное деление|Деление с остатком|\
            #                                         Возведение в спепень|Квадратный корень|\
            #                                         Предыдущее меню)$'), modules_menu)],
            # SECONDMENU: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            # SUMM: [MessageHandler(Filters.dice, input_first_num)],
            INPUTV: [MessageHandler(Filters.text & ~Filters.command, inputv_number)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    #START, FIRSTMENU, SECONDMENU, SUMM, SUB, MULT, DIV, DIV_, REM, POW, SQRT = range(11)
    dispatcher.add_handler(conv_handler)
    

    updater.start_polling()
    updater.idle()