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

    bsObj = BeautifulSoup(html.read(), "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError as e:
        print("This is missing something! No worries through!")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)"))

links = getLinks("")
if links == None:
    print("HTTPError")
else:
    for link in links:
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)