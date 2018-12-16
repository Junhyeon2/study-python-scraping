from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getTags(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    except AttributeError as e:
        return None
    return tags

tags = getTags("http://pythonscraping.com/pages/page2.html")
if tags == None:
    print("Title could not be found")
else:
    for tag in tags:
        print(tag)