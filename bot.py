import telebot
import sqlite3

bot = telebot.TeleBot('1881811910:AAFp0uLqYXkPUBYihR7QN1eHWK7KEXVdS_k')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привет" or message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
