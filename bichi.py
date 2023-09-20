# import requests

# # Define the base API URL
# url = "https://www.googleapis.com/customsearch/v1"

# # Define your API key and CX ID
# api_key = "AIzaSyDtW6x6vKWgf-MbQFWsLG5nRTYbmh0-eJQ"
# cx_id = "a5092aef863c54318"

# # Define the search query
# query = "apple"

# # Set up parameters for the API request
# params = {
#     "q": query,
#     # "num": 20,  # Number of images to fetch (adjust as needed)
#     "searchType": "image",
#     "key": api_key,
#     "cx": cx_id,
# }

# # Make the API request and store the response
# response = requests.get(url, params=params)

# results = response.json()['items']
# for item in results:
#     print(item['link'])

# # Check for a successful response and handle it accordingly
# # if response.status_code == 200:
# #     data = response.json()
# #     # Process the data as needed
# #     print(data)
# # else:
# #     print(f"Error: {response.status_code}")





import os
import requests

# Define the base API URL
url = "https://www.googleapis.com/customsearch/v1"

# Define your API key and CX ID
api_key = "AIzaSyDtW6x6vKWgf-MbQFWsLG5nRTYbmh0-eJQ"
cx_id = "a5092aef863c54318"

# Define the search query
query = "apple"

# Set up parameters for the API request
params = {
    "q": query,
    # "num": 20,  # Number of images to fetch (adjust as needed)
    "searchType": "image",
    "key": api_key,
    "cx": cx_id,
}

# Make the API request and store the response
response = requests.get(url, params=params)

# Check for a successful response
if response.status_code == 200:
    data = response.json()
    results = data.get('items', [])

    # Create a folder to save images
    save_folder = "images"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for i, item in enumerate(results):
        img_url = item['link']
        img_extension = img_url.split('.')[-1]
        img_filename = f"{i + 1}.{img_extension}"
        img_path = os.path.join(save_folder, img_filename)

        try:
            # Download and save the image
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)

            # Print the image URL
            print(f"Image {i + 1}: {img_url}")

        except Exception as e:
            print(f"Error downloading image {i + 1}: {e}")

else:
    print(f"Error: {response.status_code}")