import requests
import os
from dotenv import load_dotenv


def download_picture(image_link, filename, api_key=""):
    os.makedirs('images', exist_ok=True)
    params = {"api_key": api_key}
    response = requests.get(image_link, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


load_dotenv()
bot_token = os.environ["TELEGRAM_TOKEN"]
Nasa_api_token = os.environ["NASA_API_TOKEN"]

params = {"api_key": Nasa_api_token}
