import telebot
from telebot import types

#token
bot = telebot.TeleBot('5447921416:AAGa0EKgsllkwcbCyzPEpyJuhId5v6RdM6c')

@bot.message_handler(commands=["start"])
def start(message):
    start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    menu = types.KeyboardButton(text="📚 Меню")
    info = types.KeyboardButton(text="ℹ️ Информация")
    start.add(menu, info)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=start)


@bot.message_handler(content_types=['text'])
def menu_gl(message):
    if message.text == "📚 Меню":
        menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        website = types.KeyboardButton(text="🌐 Сайт школы")
        raspisanie = types.KeyboardButton(text="📅 Расписание")
        foto = types.KeyboardButton(text="Фотографии")
        chat = types.KeyboardButton(text="Болталка")
        sciense = types.KeyboardButton(text="👨‍🎓 Предметы")
        video = types.KeyboardButton(text="📹 Видео")
        home = types.KeyboardButton(text="🔙 Главное меню")
        menu.add(website, raspisanie, foto, chat, sciense, video, home)
        bot.send_message(message.chat.id, "Выберите раздел", reply_markup=menu)

    elif message.text == "🌐 Сайт школы":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайт школы", url="https://sch1440.mskobr.ru"))
        bot.send_message(message.chat.id, "Ссылка:", reply_markup=markup)

    elif message.text == "📹 Видео":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Школа 24 июня 2022", url="https://youtu.be/TFdqabNRnHI"))
        markup.add(types.InlineKeyboardButton("Выпускной 2022", url="https://youtu.be/1nHmkMhGDa4"))
        markup.add(types.InlineKeyboardButton("Поздравление девчонок на 23 февраля", url="https://youtu.be/nM0rY4sj1aA"))
        markup.add(types.InlineKeyboardButton("Новогодние пожелания", url="https://youtu.be/rbI3I8l9yTE"))
        markup.add(types.InlineKeyboardButton("Новогоднее поздравление 2022", url="https://youtu.be/nvfpReb0vUk"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "📅 Расписание":
        photo = open('rasp.png','rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Расписание сейчас пустое. Лето же")

    elif message.text == "👨‍🎓 Предметы":
        predmet = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        inform = types.KeyboardButton(text="Информатика")
        raspisanie = types.KeyboardButton(text="Русский язык")
        matem = types.KeyboardButton(text="Математика")
        liter = types.KeyboardButton(text="Литература")
        history = types.KeyboardButton(text="История")
        lang = types.KeyboardButton(text="Иностранные языки")
        geogr = types.KeyboardButton(text="География")
        allpredmet = types.KeyboardButton(text="Общее")
        home = types.KeyboardButton(text="🔙 Главное меню")
        predmet.add(inform, raspisanie, matem, liter, history, lang, geogr, allpredmet, home)
        bot.send_message(message.chat.id, "Выбери предмет:", reply_markup=predmet)

    elif message.text == "Информатика":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Самоучитель Python", url="http://pythontutor.ru"))
        markup.add(types.InlineKeyboardButton("Час кода", url="https://codewards.ru/hourofcode"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "Русский язык":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Правила русского языка", url="https://therules.ru"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "Литература":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Лекции по русской литературе", url="https://www.culture.ru/themes/255902/lekcii-po-russkoi-literature-dlya-shkolnikov"))
        markup.add(types.InlineKeyboardButton("Аудиокниги для 7-го класса", url="https://www.culture.ru/themes/637/audioknigi-dlya-7-go-klassa"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "История":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("История России в фотографиях", url="https://russiainphoto.ru/"))
        markup.add(types.InlineKeyboardButton("Арзамас на YouTube", url="https://www.youtube.com/channel/UCVgvnGSFU41kIhEc09aztEg"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "Математика":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Учебник. 6 класс", url="https://disk.yandex.ru/i/5Go0mTLb_vg_2g"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "Иностранные языки":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Базовая грамматика", url="https://www.duolingo.com/"))
        markup.add(types.InlineKeyboardButton("Советы по изучению английского языка", url="https://www.youtube.com/playlist?list=PLFKp3jApY_lcdamjFjn5fyKN3e3W9sP8E"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "География":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Виртуальные путешествия", url="https://www.airpano.ru"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "Общее":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("РЭШ по всем предметам 7 класса", url="https://resh.edu.ru/class/7/"))
        markup.add(types.InlineKeyboardButton("Интерактивные рабочие тетради по всем предметам", url="https://edu.skysmart.ru"))
        bot.send_message(message.chat.id, "Ссылки:", reply_markup=markup)

    elif message.text == "🔙 Главное меню":
        start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        menu = types.KeyboardButton(text="📚 Меню")
        info = types.KeyboardButton(text="ℹ️ Информация")
        start.add(menu, info)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=start)

    elif message.text == "ℹ️ Информация":
        start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        menu = types.KeyboardButton(text="📚 Меню")
        info = types.KeyboardButton(text="ℹ️ Информация")
        start.add(menu, info)
        bot.send_message(message.chat.id, "Начальник бота: Кирилл Александрович \nЕсли есть пожелания и предложения, напиши сюда: larink@mail.ru", reply_markup=start)

    else:
        bot.send_message(message.chat.id, text="Извини, на такую комманду я ещё не запрограммирован...")

bot.polling(none_stop=True)