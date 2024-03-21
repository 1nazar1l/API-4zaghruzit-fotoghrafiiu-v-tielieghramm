from telegram import Bot
import time
import os
import argparse
import random


bot_token = "7072799364:AAHgUr88fdlG9zVIJFFSP7X9rVM2DShY3i0"
bot = Bot(token=bot_token)
parser = argparse.ArgumentParser()
parser.add_argument('--time', default="14400", help='Введите с какой частотой будут отправляться картинки:')
args = parser.parse_args()
while True:
    folder = os.walk("images")
    for folder_contents in folder:
        dirpath, dirnames, filenames = folder_contents
        random.shuffle(filenames)
        for img in filenames:
            with open(f'images/{img}', 'rb') as images:
                bot.send_document(chat_id="@dwnl_img", document=images)

            time.sleep(5)
    time.sleep(args.time)
