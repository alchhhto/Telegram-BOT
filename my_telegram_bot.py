import telebot
from telebot import types
from PasswordGenerator import Password

token = "7153578431:AAFS7Kmv0xfkQLeN_pTaqZ9zcucIzBEwO5E"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.InlineKeyboardButton("Начнём!", callback_data="qwerty")
    markup.add(btn1)

    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {message.from_user.first_name}! "
        f"А вы знаете, как создать безопасный пароль для своих онлайн-аккаунтов? "
        f"Мы подготовили для вас 3 интересные функции, связанные с надежными паролями! "
        f"Попробуйте все! Авторы: Барахтенко Алёна, Сон Евгения, Шугаева Валерия, Еськова Ирина - Б3123-08.03.01",
        reply_markup=markup,
    )

    button_message(message)


@bot.message_handler(commands=["button"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.InlineKeyboardButton(
        "Как сделать надежный пароль?", callback_data="qwerty"
    )
    btn2 = types.InlineKeyboardButton(
        "Сгенерировать надежный пароль", callback_data="qwerty"
    )
    btn3 = types.InlineKeyboardButton(
        "Проверить надежность пароля", callback_data="qwerty"
    )
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Выберите необходимую функцию", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Сгенерировать надежный пароль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("7")
        btn2 = types.KeyboardButton("8")
        btn3 = types.KeyboardButton("16")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)

        bot.send_message(message.chat.id, "Выберите длину пароля", reply_markup=markup)

    elif message.text == "7":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            "Всего 7 символов? Это очень мало и ненадёжно :(",
            reply_markup=markup,
        )

    elif message.text == "8":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        password = Password()

        bot.send_message(
            message.chat.id,
            "Такая длина пароля уже подходит, но следовало бы создать пароль большей длины для безопасности онлайн-аккаунта. Держите: " + password.generate(8),
            reply_markup=markup,
        )

    elif message.text == "16":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        password = Password()

        bot.send_message(
            message.chat.id,
            "Такая длина - это то, что нужно! Держите: " + password.generate(16),
            reply_markup=markup,
        )

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.InlineKeyboardButton(
            "Как сделать надежный пароль?", callback_data="qwerty"
        )
        btn2 = types.InlineKeyboardButton(
            "Сгенерировать надежный пароль", callback_data="qwerty"
        )
        btn3 = types.InlineKeyboardButton(
            "Проверить надежность пароля", callback_data="qwerty"
        )
        markup.add(btn1, btn2, btn3)

        bot.send_message(
            message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup
        )

    elif message.text == "Проверить надежность пароля":
        a = telebot.types.ReplyKeyboardRemove()

        user_message = bot.send_message(
            message.chat.id,
            text="Напишите свой пароль",
            reply_markup=a,
        )

        bot.register_next_step_handler(user_message, check_password)

    elif message.text == "Как сделать надежный пароль?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bot.send_message(
            message.chat.id,
            text="Чтобы создать хороший пароль, необходимо минимум 8 символов! "
            "Следует использовать комбинацию букв"
            " (как строчных, так и заглавных), цифр и специальных символов. Например,"
            " можно взять первые буквы каждого слова из фразы или песни, заменив "
            "некоторые буквы на цифры или специальные символы. Например, [Ж3лезн@я "
            "3волюц1я 1$_м3рит вн1м@н1е] - это хороший пример пароля, так как он "
            "содержит комбинацию букв, цифр и специальных символов, которую будет "
            "сложно угадать или взломать. Важно создать уникальный пароль для каждого"
            " аккаунта, чтобы обеспечить безопасность ваших данных.",
            reply_markup=markup,
        )
    else:
        bot.send_message(message.chat.id, text="Бот не распознал ваше сообщение :( Повторите ещё раз")


def check_password(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(back)

    password = Password()
    bot.send_message(
        message.chat.id, text=password.check(message.text), reply_markup=markup
    )


if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
