import requests
from bs4 import BeautifulSoup
page = requests.post("https://hub.rgukt.ac.in/hub/notice/index",verify=False)
soup = BeautifulSoup(page.content,"html.parser")
html = list(soup.children)[3]
body = html.body
section = body.find("section",class_="content")
div_collapse = section.find_all("div",class_="collapse")
id_one = int([hid["id"] for hid in div_collapse][0])
print(id_one)
while True:
    try:
        page = requests.post("https://hub.rgukt.ac.in/hub/notice/index",verify=False)
        soup = BeautifulSoup(page.content,"html.parser")
        html = list(soup.children)[3]
        body = html.body
        section = body.find("section",class_="content")
        div_collapse = section.find_all("div",class_="collapse")
        id_zero = int([hid["id"] for hid in div_collapse][0])
        print(id_zero)
        if(id_zero > id_one):
            iter_ = id_zero-id_one
            card_link = section.find_all("a",class_="card-link")
            for i in range(0,iter_):
                msg_one = "Hello RGUKTIAN !!!"
                msg_two = "you have a new notice in hub regarding :)"
                card_info = card_link[i].text.replace("   ","").replace("&"," and ").strip()
                msg_three = "please visit hub for more info..."
                url="https://www.fast2sms.com/dev/bulkV2"
                message=f"{msg_one}\n{msg_two}\n\n{card_info}\n\n{msg_three}"
                number_one =7702754270
                payload_one=f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number_one}'
                headers={"authorization":"Z3j1NlfFPWODIb5exYpVRiq62tkn48h7UQyAw9MHKvdCzLaJgmtDvcrGLShRmyl0X3NznZ4CE1kKsA7O","Content-Type":"application/x-www-form-urlencoded"}
                response_one=requests.request("POST",url=url,data=payload_one,headers=headers)
                number_two =9441002256
                payload_two=f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number_two}'
                response_two=requests.request("POST",url=url,data=payload_two,headers=headers)
                number_three =7702819964
                payload_three=f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number_three}'
                response_three=requests.request("POST",url=url,data=payload_three,headers=headers)
                print(response_one.text)
                print(response_two.text)
                print(response_three.text)
            id_one = id_zero
    except:
        continue
