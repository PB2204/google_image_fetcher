# google_image_fetcher/google_image_fetcher.py

import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class GoogleImageFetcher:
    API_KEY = os.getenv("API_KEY")
    CX_ID = os.getenv("CX_ID")
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def fetch_images(self, query: str, save_folder: Optional[str] = "images"):
        """
        Fetch images from Google based on a query and save them to a specified folder.

        Args:
            query (str): The search query for images.
            save_folder (str, optional): The folder where images will be saved. Defaults to "images".
        """
        params = {
            "q": query,
            "searchType": "image",
            "key": self.API_KEY,
            "cx": self.CX_ID,
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get("items", [])

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            for i, item in enumerate(results):
                img_url = item["link"]
                img_extension = img_url.split(".")[-1]
                img_filename = f"{i + 1}.{img_extension}"
                img_path = os.path.join(save_folder, img_filename)

                try:
                    img_data = requests.get(img_url).content
                    with open(img_path, "wb") as img_file:
                        img_file.write(img_data)

                    print(f"Image {i + 1}: {img_url}")

                except Exception as e:
                    print(f"Error downloading image {i + 1}: {e}")

        else:
            print(f"Error: {response.status_code}")
