import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome_service import Service
import smtplib
from email.message import EmailMessage
import constants as con
import time

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME-BIN")
op.add_argument("-remote-debugging-port=9224")
op.add_argument("--headless")
op.add_argument("--disable-dev-sh-usage")
op.add_argument("--no-sandbox")
s = Service(os.environ.get('CHROMEDRIVER_PATH'))
#binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

class moodle(webdriver.Chrome):
    def __init__(self,service,chrome_options):
        super(moodle,self).__init__(service,chrome_options)

    def __exit__(self):
        self.close()
        self.quit()

    def login(self):
        #self.maximize_window()
        self.get(con.base_url)
        self.implicitly_wait(30)
        username = self.find_element(By.ID,"username")
        username.clear()
        username.send_keys(con.username)
        pswd = self.find_element(By.ID,"password")
        pswd.clear()
        pswd.send_keys(con.pswd)
        login = self.find_element(By.ID,"loginbtn")
        login.click()
        
    def save_changes(self):
        status = self.find_element(By.CSS_SELECTOR,".statuscol a")
        status.click()
        present = self.find_elements(By.CLASS_NAME,"form-check-input")
        present[0].click()
        submit = self.find_element(By.ID,"id_submitbutton")
        submit.click()

    def dashboard_home(self):
        dashboard = self.find_element(By.XPATH,"//*[@id='page-navbar']/nav/ol/li[1]/a")
        dashboard.click()

    def send_msg(self):
        subject_name = self.find_element(By.TAG_NAME,"h1").text
        msg = EmailMessage()
        msg.set_content(f"\nHey @Deva ( ^ ^ )\n\nAttendance was submitted\n\nDetails:\nSubject:{subject_name}:)\nStatus:present\n\nThank you........&&831!!!")
        msg['subject'] = "Your attendance result :)"
        msg['from'] = "attendence.result.bot@gmail.com"
        msg['to'] = "devaagulla770@gmail.com"
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("attendence.result.bot@gmail.com","DevarajAgulla")
        server.send_message(msg)
        server.quit()

        
    def attendance(self):
        subjects = self.find_elements(By.CSS_SELECTOR,".column a")
        for i  in range(0,len(subjects)):
            subs = self.find_elements(By.CSS_SELECTOR,".column a")
            subs[i].click()
            try:
                attendance = self.find_elements(By.CSS_SELECTOR,".modtype_attendance .aalink")
                if(len(attendance) > 0):
                    attendance[0].click()                  
                    try:
                        self.save_changes()
                        self.send_msg()
                    except:
                        self.dashboard_home()
                        continue
                self.dashboard_home()
            except:
                self.dashboard_home()    

    def logout(self):
        wait = WebDriverWait(self, 20)
        toggle_one = wait.until(ec.element_to_be_clickable((By.ID,"action-menu-toggle-1")))
        toggle_one.click()
        logout = self.find_element(By.XPATH,"//*[@id='actionmenuaction-6']")
        logout.click()
            

while True:    
    bot = moodle(service=s,chrome_options=op)
    bot.login()
    bot.attendance()
    bot.logout()
    bot.__exit__()
    time.sleep(2000)
