import requests
from tools import download_picture, params
import os
from urllib.parse import urlparse


def link_path_output(url):
    root_ext = os.path.splitext(url)
    root_ext = urlparse(root_ext[1])
    return root_ext[2]


url = "https://api.nasa.gov/planetary/apod?count=5"
response = requests.get(url, params=params)
response.raise_for_status()
for url_number, nasa_object in enumerate(response.json()):
    root_ext = link_path_output(nasa_object["url"]) #получаем разрешение картинки
    filename = f"images/nasa_apod_{url_number}{root_ext}"
    download_picture(nasa_object["url"], filename)