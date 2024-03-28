import requests
from tools import download_picture
import argparse


def main():
    parser = argparse.ArgumentParser(description="Скачивает фотографии взлета ракеты от SpaceX")
    parser.add_argument('--id', default="5eb87d47ffd86e000604b38a", help='Ваше id')
    args = parser.parse_args()
    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    response = requests.get(url)
    response.raise_for_status()
    for image_number, image_link in enumerate(response.json()["links"]["flickr"]["original"]):
        filename = f"images/spacex_{image_number}.jpg"
        download_picture(image_link, filename)


if __name__ == '__main__':
    main()

