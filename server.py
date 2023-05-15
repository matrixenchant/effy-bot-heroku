from flask import Flask, request
import telebot
from bot import bot
from config import TOKEN
import os

server = Flask(__name__)

# SERVER SIDE
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

@server.route("/")
def webhook():
   #bot.remove_webhook()
   #bot.set_webhook(url='https://effy-bot.herokuapp.com/' + TOKEN)
   return "!", 200