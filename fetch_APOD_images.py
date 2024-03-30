import requests
from tools import download_picture
import os
from urllib.parse import urlparse
import argparse
from dotenv import load_dotenv


def get_extension(url):
    root_ext = os.path.splitext(url)
    root_ext = urlparse(root_ext[1])
    return root_ext[2]


def main():
    load_dotenv()
    nasa_api_token = os.environ["NASA_API_TOKEN"]
    parser = argparse.ArgumentParser(description="Скачивает фотографии космоса с Nasa")
    parser.add_argument('--count', type=int, default="5", help='Введите количество скачиваемых картинок:')
    args = parser.parse_args()
    params = {
        "api_key": nasa_api_token,
        "count": args.count
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    for url_number, nasa_inf_block in enumerate(response.json()):
        root_ext = get_extension(nasa_inf_block["url"])
        filename = f"images/nasa_apod_{url_number}{root_ext}"
        download_picture(nasa_inf_block["url"], filename)


if __name__ == '__main__':
    main()
