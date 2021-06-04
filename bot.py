import telebot
import random
import sqlite3

bot = telebot.TeleBot('1881811910:AAFp0uLqYXkPUBYihR7QN1eHWK7KEXVdS_k')


def rrr(word):
    tgt_stress_pos = 0
    for i in word[::-1]:
        if i in 'уеыаоэяиюё':
            tgt_stress_pos -= 1
        elif i == '#':#actually wouldnt work, need to find this word in dictionary first to detect stress
            break
    print(tgt_stress_pos)
    a = []
    con = sqlite3.connect('db.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM words')
    rows = cursorObj.fetchall()
    for row in rows:
        a.append(row)

    rhymes = []

    random.shuffle(a)

    z = 0

    for i in range(len(a)):

        if a[i][0][-2:] == word[-2:]:
            cand_stress_pos = 0
            for j in a[i][0][::-1]:
                if j in 'уеыаоэяиюё':
                    cand_stress_pos -= 1
                elif j == '#':
                    break
            if cand_stress_pos != tgt_stress_pos:
                continue
            z += 1
            print(a[i][0])
            rhymes.append(a[i][0])
            if z == 3:
                return rhymes
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
        for i in range(len(rrr(src))):
            bot.send_message(message.from_user.id, *list(rrr(src)))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
