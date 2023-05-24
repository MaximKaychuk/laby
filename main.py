import telebot
from telebot import types
import requests
import psycopg2
conn = psycopg2.connect(database="database", user="postgres", password="M10112004g", host="localhost", port="5432")

cursor = conn.cursor()
cursor.execute('SELECT * FROM public.timetable_even;')
days_list = []

i = 0
for row in cursor.fetchall():
    if i % 5 == 0:
        days_list.append([row])
    else:
        days_list[-1].append(row)
    i += 1

days_names = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА']

for i, day in enumerate(days_list):
    print(days_names[i])
    pars = [[el for el in par if el is not None][0].split(', ') for par in day]
    for j, par in enumerate(pars):
        if len(set(par)) == 1:
            res = par[0]
        else:
            res = '\n'.join(par)
        print(f'{j + 1}. {res}')
    print('\n\n')

token = "5962759743:AAFs5I_bBR7GqYLerHX4pgzWY64Js1d4Bi4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею сосать хуй.')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')



bot.polling(none_stop=True)


