import requests

import deepl
API_KEY_DEEPL = "0bffab8b-8341-453a-a518-3808f64987b8:fx"
deepl_client = deepl.DeepLClient(API_KEY_DEEPL)


class SpacePhoto:
    API_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key, date):
        self.api_key = api_key
        self.date = date
        self.title = None
        self.description = None
        self.image_url = None

    def load(self):
        """Downloaded cos photo from NASA API"""
        params = {
            "api_key": self.api_key, 
            "date": self.date
        }

        response = requests.get(self.API_URL, params=params)
        data = response.json()

        self.title = data.get("title", "No name")
        self.description = data.get("explanation", "No Description")
        self.image_url = data.get("url", "")

        self.description = deepl_client.translate_text(self.description, target_lang="UK")


    def show_info(self):
        """Info about the photo"""
        print("Photo For NASA")
        print("Name:", self.title)
        print("\n discription:")
        print(self.description)
        print("\n check the photo:")
        print(self.image_url)