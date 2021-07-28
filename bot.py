import telebot
import os
import uuid
from flask import Flask, request

token = '1946015248:AAGwjZCmr5stnb3hQun7ekYIdml-DymfLIs'
#https://api.telegram.org/bot1946015248:AAGwjZCmr5stnb3hQun7ekYIdml-DymfLIs/setWebhook?url=url
'''server = Flask(__name__)'''
bot = telebot.TeleBot(token, parse_mode=None)

'''@server.route("/", methods=["POST"])
def receive_update():
 bot.process_new_updates(
  [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
 )
 return {'ok':True}'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, message.text)


'''@server.route("/" + token, methods=["POST"])
def getMessage():
 bot.process_new_updates(
  [
   telebot.types.Update.de_json(
    request.stream.read().decode("utf-8")
   )
  ]
 )
 return "!", 200'''

'''if name == "__main__":
 server.run()'''


bot.polling()









