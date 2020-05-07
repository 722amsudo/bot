import telebot
from creds import bot_id12

bot = telebot.TeleBot(bot_id12)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['ali', 'help', 'psi', 'sag', 'temp'])
def send_text(message):

	if message.text == "/ali":
		bot.send_message(message.from_user.id, "going to ali page")

	elif message.text == "/help":
		bot.send_message(message.from_user.id, "list of commands")

	elif message.text == "/psi":
	   	bot.send_message(message.from_user.id, "psi to bar calc")

	elif message.text == "/sag":
	   	bot.send_message(message.from_user.id, "sag per travel calc")

	elif message.text == "/temp":
	   	bot.send_message(message.from_user.id, "temp difference")

	else:
	  	bot.send_message(message.from_user.id, "for list of commands type /help.")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "for list of commands type /help.")



bot.polling()

