import telebot

bot = telebot.TeleBot('7836311040:AAGWUXP_19blFt4fg9Fyeu57KKjTyNZdHLQ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi!", parse_mode='html')

@bot.message_handler(content_types=['text'])  # Content types should be in list format
def echo(message):
    bot.send_message(message.chat.id, message.text, parse_mode='html')

bot.infinity_polling()
