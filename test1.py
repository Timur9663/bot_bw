import telebot
import os
from flask import Flask, request
from PIL import Image,ImageFilter
from io import BytesIO


token = "1946015248:AAGwjZCmr5stnb3hQun7ekYIdml-DymfLIs"

'''server = Flask(name)'''
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['photo'])
def echo_all(message):
    # Получаем id фотографии в Telegram
    photo_id = message.photo[-1].file_id
    # Достаём картинку
    photo_file = bot.get_file(photo_id) # <class 'telebot.types.File'>
    photo_bytes = bot.download_file(photo_file.file_path) # <class 'bytes'>
   
#    Класс io.BytesIO() реализация потока, использующая буфер байтов в памяти. 
#    Класс io.BytesIO наследует 
#    io.BufferedIOBase. Буфер отбрасывается при вызове метода close().
    stream = BytesIO(photo_bytes)
    image = Image.open(stream).convert("RGBA")
    stream.close()

    image.show()
    image.save("C:/Users/admin/projects/result_image/rezolution.png")
    size = (128, 128)
    png = Image.open("C:/Users/admin/projects/result_image/rezolution.png")
    png.thumbnail(size)
    png.save("res.png")
    png.show()
    bot.send_photo(message.chat.id, photo=png)
    # размываем изображение
    # blurred = image.filter(ImageFilter.CONTOUR)
    # # открываем оригинал и размытое изображение
    # image.show()
    # blurred.show()
    # # сохраняем изображение
    # png.save("C:/Users/User/new1/result_im/blur.png")
    # bot.send_photo(message.chat.id, photo=image)

# миниатюра 
    # size = (128, 128)
# saved = "lenna.jpeg"
# img = Image.open("Lenna.png")
# img.thumbnail(size)
# img.save(saved)
# img.show()
# --------------
# CONTOUR 

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

bot.polling()


