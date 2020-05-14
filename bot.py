import telebot
from creds import bot_id12
from psikpi import *
from kglbs import *

bot = telebot.TeleBot(bot_id12)

#function that runs if /kglbs is called

def fun_kglbs():
	bot.send_message(message.from_user.id, "going to test function")





@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['kglbs', 'help', 'psi', 'sag', 'temp'])
def send_text(message):

	if message.text == "/kglbs":
		fun_kglbs()

	elif message.text == "/help":
		bot.send_message(message.from_user.id, "list of commands: /kglbs, /psi, /sag, /temp")

	elif message.text == "/psi":
	   	bot.send_message(message.from_user.id, "psi to bar calc", psikpifunct ())

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

