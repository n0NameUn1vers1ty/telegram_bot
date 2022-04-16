import telebot

import requests
from bs4 import BeautifulSoup
import config
print('---bot started working\n---to turn off [ctrl + c]')

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])# Приветствие
def send_welcome(message):
    bot.reply_to(message, "Im working")

@bot.message_handler(commands=['itnews'])

def ItNew(message):# Парсер habr.ru
    url = 'https://habr.com/ru/news/' # Ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a', class_='tm-article-snippet__title-link',limit = 10)

    for a in links:
        temp = "https://habr.com" + a['href']
        bot.send_message(message.chat.id,temp)



@bot.message_handler(commands=['news'])

def News(message):# Парсер Lenta.ru
    bot.reply_to(message, "Новости с Lenta.ru")
    url = 'https://lenta.ru/' # Ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('span',class_="card-mini__title", limit = 10)

    for span in articles:
        bot.send_message(message.chat.id, span.text)

# RUN
bot.infinity_polling(timeout=10, long_polling_timeout = 5)
