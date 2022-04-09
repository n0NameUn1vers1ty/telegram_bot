import telebot

import requests
from bs4 import BeautifulSoup
import config
print('---bot started working\n---to turn off [ctrl + c]')

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Im working")

@bot.message_handler(commands=['iTnews'])


def ItNew(message):
    url = 'https://droider.ru/' # ссылка на сайт
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a',class_='micronews-slider__item micronews-slider__item_link')

    
    for a in links:
         bot.send_message(message.chat.id, a['href'])

    


# RUN
bot.polling(none_stop=True)
