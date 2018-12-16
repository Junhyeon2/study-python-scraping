from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getImages(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    except AttributeError as e:
        return None
    return images

images = getImages("http://pythonscraping.com/pages/page3.html")
if images == None:
    print("Title could not be found")
else:
    for image in images:
        print(image["src"])