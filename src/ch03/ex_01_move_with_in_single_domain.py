from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getLinks(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        links = bsObj.findAll("a")
    except AttributeError as e:
        return None
    return links

links = getLinks("http://en.wikipedia.org/wiki/Kevin_Bacon")
if links == None:
    print("Title could not be found")
else:
    for link in links:
        if 'href' in link.attrs:
            print(link.attrs['href'])