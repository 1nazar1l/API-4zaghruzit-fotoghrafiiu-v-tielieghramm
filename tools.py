import requests
import os


def download_picture(image_link, filename, api_key=""):
    os.makedirs('images', exist_ok=True)
    params = {"api_key": api_key}
    response = requests.get(image_link, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
