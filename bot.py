﻿import telebot
from creds import bot_id12
from psikpi import *

bot = telebot.TeleBot(bot_id12)

test_f = "fffff"
test_p = "ppppp"
test_z = "zzzzz"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['ali', 'ppp', 'zzz'])
def send_text(message):

	if message.text == "/ali":
		bot.send_message(message.from_user.id, test_f)
		
	elif message.text == "/ppp":
		bot.send_message(message.from_user.id, test_p)
		
	elif message.text == "/zzz":
		bot.send_message(message.from_user.id, test_z)	

	else:
	  	bot.send_message(message.from_user.id, "for list of commands type /help.")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "for list of commands type /help.")



bot.polling()

