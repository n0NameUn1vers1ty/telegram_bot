import telebot

import config
print('---bot started working\n---to turn off [ctrl + c]')

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])

def lala(message):
    bot.send_message(message.chat.id, message.text)


# RUN
bot.polling(none_stop=True)
