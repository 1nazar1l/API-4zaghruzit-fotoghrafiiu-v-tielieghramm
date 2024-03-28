from telegram import Bot
import time
import os
import argparse
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot_token = os.environ["TELEGRAM_TOKEN"]
    bot = Bot(token=bot_token)
    parser = argparse.ArgumentParser(description="Отправляет фотографии в ТГ канал")
    parser.add_argument('--time', type=int, default="14400", help='Введите с какой частотой будут отправляться картинки:')
    parser.add_argument("chat_id", type=str, help="Введите id своего ТГ канала:")
    args = parser.parse_args()
    while True:
        folder = os.walk("images")
        for folder_contents in folder:
            dirpath, dirnames, filenames = folder_contents
            random.shuffle(filenames)
            for img in filenames:
                with open(f'images/{img}', 'rb') as images:
                    bot.send_document(chat_id=args.chat_id, document=images)

                time.sleep(5)
        time.sleep(args.time)


if __name__ == '__main__':

    main()
