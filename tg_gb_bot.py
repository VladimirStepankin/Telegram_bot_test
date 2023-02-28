import telebot
from random import *
import json
import requests

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Фильмотека успешно сохранена в файле films.json")


def load():
    try:
        global films
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена")
    except:
        films = []
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властилин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара")
        print("Фильмотека была загружена по умолчанию")
        print(films)


'''
while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите еще, будем рады!")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f = input("Введите название фильма ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию")
    elif command == "/help":
        print("Здесь какой-то мануал")
    elif command == "/delete":
        f = input("Введите название фильма, который хотите удалить ")
        try:
            films.remove(f)
            print("Фильм был успешно удален!")
        except:
            print("Такого фильма нет в коллекции")
    elif command == "/random":
        # rnd=randint(0,len(films)- 1)
        # print("Слепой жребий показал вам фильм - " + films[rnd])
        print("Слепой жребий показал вам фильм - " + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")
'''
API_TOKEN = '5762732060:AAE1MnHUXOBb1LvBBLP6hwXYpJLFKa0hez4'
bot = telebot.TeleBot(API_TOKEN)
API_URL = 'https://7012.deeppavlov.ai/model'


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Фильмотека была успешно загружена")
    except:
        films = []
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властилин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара")
        bot.send_message(message.chat.id, "Фильмотека загружена по умолчанию")


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, "Вот список фильмов")
    bot.send_message(message.chat.id, ", ".join(films))


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то ничего не нашел")


bot.polling()
