import requests
from bs4 import BeautifulSoup
import time
page = requests.get("http://devadas.me/myportfolio/",verify=False)
soup = BeautifulSoup(page.content,"html.parser")
html = list(soup.children)[2]
body = html.body
section = body.find_all("section",class_="tezt")
one = int(section[0]["id"])
while True:
    try:
        page = requests.get("http://devadas.me/myportfolio/",verify=False)
        soup = BeautifulSoup(page.content,"html.parser")
        html = list(soup.children)[2]
        body = html.body
        section = body.find_all("section",class_="tezt")
        zero = int(section[0]["id"])
        if (zero>one):
            iter_ = zero-one
            for i in range(0,iter_):
                print(int(section[i]["id"]))
                time.sleep(6)
            one = zero
        print("over")
        time.sleep(6)
    except:
        continue
    


    
