# google_image_fetcher

Google Image Fetcher is a Python library that allows you to fetch images from Google Search using the Custom Search JSON API.

## Motive Of The Project

Frontend Developers faces a problem , when they develop any website , that is IMAGE . All the time , they have to go to Google , to search and download the images , they want to use this in their website , when there is no Graphic Designer available in their team . As a Frontend Developer , I also faces the same problem . To solve this problem here you have this Python Library .

I want to develop this library for non-python programmers also . Here You can use this library , without any knowledge of Python Programming .

Here after following all the steps , you will be able to use the images , which will be downloaded according to your prompt / query . Also you can see the `URL` of those images in the terminal below .

## Structure Of The Project

```bash
google_image_fetcher/
│
├── google_image_fetcher/
│   ├── __init__.py
│   └── google_image_fetcher.py
│
├── CONTRIUTING.md
├── LEARN.md
├── LICENSE
├── README.md
└── setup.py
```

## setup.py

```bash
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.0'
DESCRIPTION = 'Fetch & Download Images From Google'
LONG_DESCRIPTION = 'Google Image Fetcher is a Python library that allows you to fetch images from Google Search using the Custom Search JSON API.'

# Setting up
setup(
    name="google_image_fetcher",
    version=VERSION,
    author="PB2204 (Pabitra Banerjee)",
    author_email="<rockstarpabitra2204@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests','python-dotenv'],
    keywords=['python', 'image', 'fetch', 'web scrapping', 'image scrapping'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
```

## Installation

You can install this library using pip:

```bash
pip install google_image_fetcher
```

or

```bash
pip install google-image-fetcher
```

Then You've to create new python `(.py)` file in the same folder , you're working in the Frontend / Full-Stack project .

Then You've to copy the following lines of code to your `.py` file .

```bash
from google_image_fetcher.google_image_fetcher import GoogleImageFetcher

# Create a GoogleImageFetcher instance
fetcher = GoogleImageFetcher()

# Define the search query
query = "YOUR_QUERY"

# Fetch and save images
fetcher.fetch_images(query, save_folder="YOUR_FOLDER NAME")
```

You just need to substitute `YOUR_QUERY` to your required `Image Name` and the `YOUR_FOLDER NAME` to , where you want to download the images , which will be created inside the same folder, where you're currently working . This is so simple to use .

Now you're ready to use the images .

## Contribution

If you want to contribute something please follow the [CONTRIUTING.md](https://github.com/PB2204/google_image_fetcher/blob/main/CONTRIBUTING.md).

# Happy Coding 🚀
