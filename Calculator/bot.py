import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

FIRSTMENU, SECONDMENU = random()

def start(update, _):
    reply_keyboard = [['Вещественные числа', 'Комплексные числа']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в калькулятор '
        'Команда /cancel, остановить работу.\n\n'
        'Выберите, с каким видом чисел мы будем работать',
        reply_markup=markup_key,)
    user = update.message.from_user  
    # logger.info("Знак зодиака %s: %s", user.first_name, update.message.text)
    if user == 'Вещественные числа':
        return FIRSTMENU
    elif user == 'Комплексные числа':
        return SECONDMENU

def first_menu(update, _):
    reply_keyboard = [['Cумма', 'Разность', 'Умножение'],
                    ['Деление', 'Целочисленное деление', 'Деление с остатком'],
                    ['Возведение числа в спепень числа', 'Квадратный корень числа'],
                    ['Предыдущее меню']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выберите арифметическое действие',
        reply_markup=markup_key,)
    user = update.message.from_user
  
    update.message.reply_text(
        'Хорошо. Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.',
        reply_markup=ReplyKeyboardRemove(),)
    return PHOTO


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
            SIGN: [MessageHandler(Filters.regex('^(Овен|Телец|Близнецы|Рак|Лев|Дева|Весы|Скорпион|Козерог|Водолей|Рыбы|Стрелец)$'), sign)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )