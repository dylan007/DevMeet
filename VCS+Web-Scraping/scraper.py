from bs4 import BeautifulSoup
import urllib.request
import requests

## Base URL for all XKCD Comics
url = "https://xkcd.com/"

## Taking user input for comic number to scrape
n = int(input())

## Generating URL for comicUrl
url_to_get = url + str(n)

## Getting page content using requests.get
page = requests.get(url_to_get).content

## Parsing the page as BeautifulSoup Object
soup = BeautifulSoup(page , "html.parser")

## Finding div element with id 'comic'
ImageDiv = soup.find("div",{"id":"comic"})

## Extracting image url from dictionary
comicImageTag = ImageDiv.find("img")
comicUrl = comicImageTag['src']

## Printing image url
print("https:" + comicUrl)

## Downloading imahe using urllib
filename = "comic" + str(n) + ".jpg"
urllib.request.urlretrieve("https:" + comicUrl , filename)
