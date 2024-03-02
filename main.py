import requests
import os
from urllib.parse import urlparse


def download_picture(image_link, filename, api_key = ""):
    params = {"api_key": api_key}
    response = requests.get(image_link, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    for image_number, image_link in enumerate(response.json()["links"]["flickr"]["original"]):
        filename = f"images/spacex_{image_number}.jpg"
        download_picture(image_link, filename)


def link_path_output(url):
    root_ext = os.path.splitext(url)
    root_ext = urlparse(root_ext[1])
    return root_ext[2]


Api_token = "rIKZaIP0K4FUmPnwDpuu0Bn1BISWD2SdJbaRCTpX"
params = {"api_key": Api_token}
# url = "https://api.nasa.gov/planetary/apod?count=30"
# response = requests.get(url, params=params)
# response.raise_for_status()
# for url_number, nasa_object in enumerate(response.json()):
#     root_ext = link_path_output(nasa_object["url"])#получаем разрешение картинки
#     filename = f"images/nasa_apod_{url_number}{root_ext}"
#     print(nasa_object["url"])
    # download_picture(nasa_object["url"], filename)

epic_url = "https://api.nasa.gov/EPIC/api/natural/images?"
response = requests.get(epic_url, params=params)
response.raise_for_status()
for number, object in enumerate(response.json()):
    image = object["image"]
    splited_image = image.split("_")
    date = splited_image[2]
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    full_date = f"{year}/{month}/{day}"
    planet_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{full_date}/png/{image}.png"
    filename = f"images/epic_photo_{number}.png"
    download_picture(planet_image_url, filename, Api_token)


# for number, objects in enumerate(response.json()):
#     print(response.json()[number]["url"])
# id = "5eb87d47ffd86e000604b38a"
# url = f"https://api.spacexdata.com/v5/launches/{id}"
# link_path_output(response.json())
# fetch_spacex_last_launch(url)

