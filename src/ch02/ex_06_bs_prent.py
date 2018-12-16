from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getImg(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        img = bsObj.find("img", {"src": "../img/gifts/img1.jpg"})
    except AttributeError as e:
        return None
    return img

img = getImg("http://pythonscraping.com/pages/page3.html")
if img == None:
    print("Title could not be found")
else:
    print(img.parent.previous_sibling.get_text())