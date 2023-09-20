from google_image_fetcher.google_image_fetcher import GoogleImageFetcher

# Create a GoogleImageFetcher instance
fetcher = GoogleImageFetcher()

# Define the search query
query = "cats"

# Fetch and save images
fetcher.fetch_images(query, save_folder="images")