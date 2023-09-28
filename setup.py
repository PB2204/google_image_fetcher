from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "2.0.0"
DESCRIPTION = "Fetch & Download Images From Google"
LONG_DESCRIPTION = "Google Image Fetcher is a Python library that allows you to fetch images from Google Search using the Custom Search JSON API."

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
    install_requires=["requests", "python-dotenv"],
    keywords=["python", "image", "fetch", "web scrapping", "image scrapping"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
