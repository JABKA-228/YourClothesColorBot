import telebot
import random
import sqlite3

bot = telebot.TeleBot('1881811910:AAFp0uLqYXkPUBYihR7QN1eHWK7KEXVdS_k')


def rrr(word):
    a = []
    con = sqlite3.connect('db.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM words')
    rows = cursorObj.fetchall()
    for row in rows:
        a.append(row)

    rhymes = []

    z = 0
    l = 0

    #print(a[1][0][-2:])

    for i in range(len(a)):
        if a[i][0][-2:] == word[-2:]:
            z += 1
            rhymes.append(a[i])
            if z == 3:
                #print(rhymes)
                return rhymes
    #print(rhymes)
    return rhymes



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привет" or message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "напиши привет")
    elif message.text == '/start':
        bot.send_message(message.from_user.id,
                         "Здравствуйте, вы обратились к боту, который рифмует слова. Напишите /rhyme, которому хотите подобрать рифму")
    elif message.text[:6] == '/rhyme':
        src = message.text[7:]
        bot.send_message(message.from_user.id, *list(rrr(src)))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

