from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

global pages
pages = set()

def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org" + articleUrl)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)"))
    except AttributeError as e:
        return None
    return links

links = getLinks("")
if links == None:
    print("Title could not be found")
else:
    for link in links:
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)