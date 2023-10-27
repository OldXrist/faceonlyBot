import config
import telebot
import re
import random
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Получить скидку")
    markup.add(btn1)

    bot.send_message(message.chat.id, "Добрый день ✨ \nПриветствуем вас от всей команды The Face Only! \nДля того, чтобы получить промокод на скидку 30%, подпишитесь на наш канал 🙌🏼", reply_markup=markup)
    bot.send_message(message.chat.id, "t.me/thefaceonlyrnd")


@bot.message_handler(content_types=['text'])
def sublink(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Получить скидку")
    markup.add(btn)

    if message.chat.type == 'private':
        if message.text == 'Получить скидку':
            uid = message.from_user.id
            chat_id = '@thefaceonlyrnd'
            mem = bot.get_chat_member(chat_id, uid)

            def get_substrings(string):
                return re.split('\W+', string)

            def get_distance(s1, s2):
                d, len_s1, len_s2 = {}, len(s1), len(s2)
                for i in range(-1, len_s1 + 1):
                    d[(i, -1)] = i + 1
                for j in range(-1, len_s2 + 1):
                    d[(-1, j)] = j + 1
                for i in range(len_s1):
                    for j in range(len_s2):
                        if s1[i] == s2[j]:
                            cost = 0
                        else:
                            cost = 1
                        d[(i, j)] = min(
                            d[(i - 1, j)] + 1,
                            d[(i, j - 1)] + 1,
                            d[(i - 1, j - 1)] + cost)
                        if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                            d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)
                return (d[len_s1 - 1, len_s2 - 1])

            def check_substring(search_request, original_text, max_distance):
                substring_list_1 = get_substrings(search_request)
                substring_list_2 = get_substrings(original_text)

                not_found_count = len(substring_list_1)

                for substring_1 in substring_list_1:
                    for substring_2 in substring_list_2:
                        if get_distance(substring_1, substring_2) <= max_distance:
                            not_found_count -= 1

                if not not_found_count:
                    return True

            original_text = str(mem)

            result1 = check_substring('member', original_text, max_distance=2)
            result2 = check_substring('administrator', original_text, max_distance=2)

            num = random.randint(1, 99999)
            if num < 10:
                num = ('0000' + str(num))
            elif 10 <= num < 100:
                num = ('000' + str(num))
            elif 100 <= num < 1000:
                num = ('00' + str(num))
            elif 1000 <= num < 10000:
                num = ('0' + str(num))
            promo = ('*TFO*' + str(num))

            if result1 is True:
                markup = types.ReplyKeyboardRemove(selective=False)
                bot.send_message(message.chat.id, promo +" — ваш единоразовый промокод на скидку 30% 🤍 \n\nЧтобы воспользоваться промокодом, покажите этот чат с ботом администратору перед процедурой 🙏🏼 \n\n*Важно: промокод действует 1 месяц после момента получения* \n\nЗаписаться можно по ссылке ниже 👇🏼 \n\n*Онлайн-запись* \nhttps://www.salon1c.ru/widget-org/812443398 \n\nИли напишите нам в WhatsApp 👇🏼 \n*WhatsApp* \nhttps://wa.me/78633332992 \n\nДо встречи в The Face Only 🤍", reply_markup=markup, parse_mode='markdown')
            elif result2 is True:
                markup = types.ReplyKeyboardRemove(selective=False)
                bot.send_message(message.chat.id, promo +" — ваш единоразовый промокод на скидку 30% 🤍 \n\nЧтобы воспользоваться промокодом, покажите этот чат с ботом администратору перед процедурой 🙏🏼 \n\n*Важно: промокод действует 1 месяц после момента получения* \n\nЗаписаться можно по ссылке ниже 👇🏼 \n\n*Онлайн-запись* \nhttps://www.salon1c.ru/widget-org/812443398 \n\nИли напишите нам в WhatsApp 👇🏼 \n*WhatsApp* \nhttps://wa.me/78633332992 \n\nДо встречи в The Face Only 🤍", reply_markup=markup, parse_mode='markdown')
            else:
                bot.send_message(message.chat.id, "Мы пришлём вам промокод на скидку 30% после подписки на канал 🤍")




bot.polling(none_stop=True)
