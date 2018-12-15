from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getName(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        name = bsObj.find("span", {"class": "green"})
    except AttributeError as e:
        return None
    return name

name = getName("http://pythonscraping.com/pages/warandpeace.html")
if name == None:
    print("Title could not be found")
else:
    print(name.get_text())