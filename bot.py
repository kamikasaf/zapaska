import telebot

from telebot import types


bot = telebot.TeleBot("5460644351:AAHh_rVRdBcqtfnL_Xs-sZHikmvNejs1KA8")



@bot.message_handler(commands=["start"])
def start(message):

    mess = f"Здравствуйте  <b>{message.from_user.first_name},  <u>{message.from_user.last_name},  используйте  коману  /CommandList  чтобы  узнать  что  я  умею</u> </b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["Категории"])
def python_D1(message):

    python = "Категории"

    python_ = types.InlineKeyboardMarkup(row_width=2)
    python_.add(types.InlineKeyboardButton("Категории", url="http://127.0.0.1:8000/category/"))
    
    bot.send_message(message.chat.id, python, reply_markup=python_)


@bot.message_handler(commands=["Продукты"])
def python_D2(message):

    python = "Продукты"


    python_ = types.InlineKeyboardMarkup(row_width=2)
    python_.add(types.InlineKeyboardButton("Продукты", url="http://127.0.0.1:8000/products/"))

    #__________________#
    bot.send_message(message.chat.id, python, reply_markup=python_)



@bot.message_handler(commands=["Регистрация"])
def python_D3(message):

    python = "Регистрация"


    python_ = types.InlineKeyboardMarkup(row_width=2)
    python_.add(types.InlineKeyboardButton("Регистрация", url="http://127.0.0.1:8000/account/register/"))

    #__________________#
    bot.send_message(message.chat.id, python, reply_markup=python_)


@bot.message_handler(commands=["Авторизация"])
def python_D4(message):

    python = "Авторизация"


    python_ = types.InlineKeyboardMarkup(row_width=2)
    python_.add(types.InlineKeyboardButton("Авторизация", url="http://127.0.0.1:8000/account/login/"))

    #__________________#
    bot.send_message(message.chat.id, python, reply_markup=python_)

@bot.message_handler(commands=["Выйти из аккаунта"])
def python_D5(message):

    python = "Выйти из аккаунта"

    python_ = types.InlineKeyboardMarkup(row_width=2)
    python_.add(types.InlineKeyboardButton("Выйти из аккаунта", url="http://127.0.0.1:8000/account/logout/"))

    #__________________#
    bot.send_message(message.chat.id, python, reply_markup=python_)

@bot.message_handler(commands=["CommandList"])
def knopka(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1=types.KeyboardButton("Категории")
    item2=types.KeyboardButton("Продукты")
    item3=types.KeyboardButton("Регистрация")
    item4=types.KeyboardButton("Авторизация")
    item5=types.KeyboardButton("Выйти из аккаунта")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types="text")
def buttons(message):
    if message.text == "Категории":
        return python_D1(message)
    elif message.text == "Продукты":
        return python_D2(message)
    elif message.text == "Регистрация":
        return python_D3(message)
    elif message.text == "Авторизация":
        return python_D4(message)
    elif message.text == "Выйти из аккаунта":
        return python_D5(message)
    # elif message.text == "":
    #     return python_D6(message)
    else:
        bot.send_message(message.chat.id, "я не понял что вы имели ввиду,  используйте  коману  /CommandList  чтобы  узнать  что  я  умею")


bot.polling(non_stop=True)