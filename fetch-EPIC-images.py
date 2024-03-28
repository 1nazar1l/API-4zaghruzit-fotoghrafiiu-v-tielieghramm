import requests
from tools import download_picture, params, Nasa_api_token


def main():
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
        download_picture(planet_image_url, filename, Nasa_api_token)


if __name__ == '__main__':
    main()
