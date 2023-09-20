# google_image_fetcher/google_image_fetcher.py

import os
import requests

class GoogleImageFetcher:
    def __init__(self, api_key="AIzaSyDtW6x6vKWgf-MbQFWsLG5nRTYbmh0-eJQ", cx_id="a5092aef863c54318"):
        self.url = "https://www.googleapis.com/customsearch/v1"
        self.api_key = api_key
        self.cx_id = cx_id

    def fetch_images(self, query, save_folder="images"):
        params = {
            "q": query,
            "searchType": "image",
            "key": self.api_key,
            "cx": self.cx_id,
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get('items', [])

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            for i, item in enumerate(results):
                img_url = item['link']
                img_extension = img_url.split('.')[-1]
                img_filename = f"{i + 1}.{img_extension}"
                img_path = os.path.join(save_folder, img_filename)

                try:
                    img_data = requests.get(img_url).content
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)

                    print(f"Image {i + 1}: {img_url}")

                except Exception as e:
                    print(f"Error downloading image {i + 1}: {e}")

        else:
            print(f"Error: {response.status_code}")