from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getNameList(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("span", {"class": "green"})
    except AttributeError as e:
        return None
    return nameList

nameList = getNameList("http://pythonscraping.com/pages/warandpeace.html")
if nameList == None:
    print("Title could not be found")
else:
    for name in nameList:
        print(name.get_text())