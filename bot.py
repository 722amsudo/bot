import telebot
from creds import bot_id12

bot = telebot.TeleBot(bot_id12)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "test mode on?")

bot.polling()

