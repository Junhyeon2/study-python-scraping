from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getGiftList(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        giftList = bsObj.find("table", {"id": "giftList"})
    except AttributeError as e:
        return None
    return giftList

giftList = getGiftList("http://pythonscraping.com/pages/page3.html")
if giftList == None:
    print("Title could not be found")
else:
    for child in giftList.children:
        print(child)