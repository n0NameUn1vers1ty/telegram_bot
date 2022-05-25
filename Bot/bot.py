import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup
import config
print('---bot started working\n---to turn off [ctrl + c]')

bot = telebot.TeleBot(config.TOKEN)
 

@bot.message_handler(commands=['ИТновости'])

def ItNew(message):# Парсер habr.ru
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url = 'https://habr.com/ru/news/' # Ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a', class_='tm-article-snippet__title-link',limit = 10)

    temp = "Новости с Habr" + '\n'
    temp += "https://habr.com/ru/news/"+ '\n'+ '\n'
    for a in links:
        temp += " * " + a.string + ": " + "https://habr.com"+ a['href'] + '\n'+ '\n'

    btn1 = types.KeyboardButton("/Главная")
    btn2 = types.KeyboardButton("/Новости")
    btn3 = types.KeyboardButton("/ИТновости")
    btn4 = types.KeyboardButton("/Погода")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id,temp,disable_web_page_preview=True,disable_notification=True)



@bot.message_handler(commands=['Новости'])

def News(message):# Парсер Lenta.ru
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url = 'https://lenta.ru/' # Ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    firstTopic = soup.find('div',class_='card-big__titles')
    firstTopicLink = soup.find('a', class_ = 'card-big _topnews _news')
    topics = soup.find_all('span',class_='card-mini__title', limit = 10)
    topicsLinks = soup.find_all('a',class_='card-mini _topnews', limit = 10)

    temp = "Новости с Lenta.ru" + '\n' + '\n'
    temp += " * " + firstTopic.string + ": " + "https://lenta.ru" + firstTopicLink['href'] + '\n'+'\n'
    i = 0
    for span in topics:
        temp += " * " + span.text+ ": " + "https://lenta.ru" + topicsLinks[i]['href'] +'\n'+'\n'
        i = i + 1

    btn1 = types.KeyboardButton("/Главная")
    btn2 = types.KeyboardButton("/Новости")
    btn3 = types.KeyboardButton("/ИТновости")
    btn4 = types.KeyboardButton("/Погода")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, temp, disable_notification=True, disable_web_page_preview=True,reply_markup=markup)



@bot.message_handler(commands=['Погода'])

def Weather(message):# Парсер погоды
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url = 'https://world-weather.ru/pogoda/russia/moscow/' # Ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    delete = soup.find('span',id='open-desc-weather')
    delete.clear()
    delete = soup.find('span',id='close-desc-weather')
    delete.clear()
    weather = soup.find('span',class_='dw-into')
    
    

    temp = "Погода сегодня" + '\n' + '\n'
    temp += weather.text + '\n'+ '\n'
    temp += "https://world-weather.ru/pogoda/russia/moscow/"

    btn1 = types.KeyboardButton("/Главная")
    btn2 = types.KeyboardButton("/Новости")
    btn3 = types.KeyboardButton("/ИТновости")
    btn4 = types.KeyboardButton("/Погода")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, temp, disable_notification=True, disable_web_page_preview=True,reply_markup=markup)

@bot.message_handler(commands=['start','Главная'])

def intro(message):#Общее сообщение
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url1 = 'https://world-weather.ru/pogoda/russia/moscow/' # Ссылка на сайт
    url2 = 'https://lenta.ru/' # Ссылка на сайт
    url3 = 'https://habr.com/ru/news/' # Ссылка на сайт
    response = requests.get(url1)
    soup1 = BeautifulSoup(response.text, 'lxml')
    response = requests.get(url2)
    soup2 = BeautifulSoup(response.text, 'lxml')
    response = requests.get(url3)
    soup3 = BeautifulSoup(response.text, 'lxml')
    #погода
    delete = soup1.find('span',id='open-desc-weather')
    delete.clear()
    delete = soup1.find('span',id='close-desc-weather')
    delete.clear()
    weather = soup1.find('span',class_='dw-into')
    
    temp1 = weather.text
    temp2 = temp1[0:154]

    temp = "Погода сегодня" + '\n'
    temp += temp2 + '\n'+ '\n'

    #Lenta.ru
    temp += "Lenta.ru" + '\n'
    firstTopic = soup2.find('div',class_='card-big__titles')
    firstTopicLink = soup2.find('a', class_ = 'card-big _topnews _news')
    temp += " * " + firstTopic.string + ": " + "https://lenta.ru" + firstTopicLink['href'] + '\n'+'\n'
    topics = soup2.find_all('span',class_='card-mini__title', limit = 3)
    topicsLinks = soup2.find_all('a',class_='card-mini _topnews', limit = 3)
    i = 0
    for span in topics:
        temp += " * " + span.text+ ": " + "https://lenta.ru" + topicsLinks[i]['href'] +'\n'+'\n'
        i = i + 1
    temp += '\n'+ '\n'

    #Хабр
    temp += "Хабр" + '\n'
    links = soup3.find_all('a', class_='tm-article-snippet__title-link', limit = 4)
    for a in links:
        temp += " * " + a.string + ": " + "https://habr.com"+ a['href'] + '\n'+ '\n'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Главная")
    btn2 = types.KeyboardButton("/Новости")
    btn3 = types.KeyboardButton("/ИТновости")
    btn4 = types.KeyboardButton("/Погода")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, temp, disable_notification=True, disable_web_page_preview=True,reply_markup=markup)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)
