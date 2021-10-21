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
                url="https://www.fast2sms.com/dev/bulkV2"
                message = "f{i}"
                number = 7702754270
                payload_one=f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number}'
                headers={"authorization":"Z3j1NlfFPWODIb5exYpVRiq62tkn48h7UQyAw9MHKvdCzLaJgmtDvcrGLShRmyl0X3NznZ4CE1kKsA7O","Content-Type":"application/x-www-form-urlencoded"}
                response_one=requests.request("POST",url=url,data=payload_one,headers=headers)
                print(response_one.text)
            one = zero
        print("over")
        time.sleep(6)
    except:
        continue
    


    
