import os
from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#op.add_argument("-remote-debugging-port=9224")
op.add_argument("--headless")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--no-sandbox")
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
"""options = webdriver.FirefoxOptions()
options.log.level = "trace"
options.add_argument("-remote-debugging-port=9224")
options.add_argument("-headless")
#options.add_argument("-disable-gpu")
#options.add_argument("-no-sandbox")

binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))


driver = webdriver.Firefox(firefox_binary=binary,executable_path=os.environ.get('GECKODRIVER_PATH'),options=options)"""
driver.maximize_window()
driver.get("http://lms.rgukt.ac.in/login/index.php")
driver.implicitly_wait(30)
#login script
username = driver.find_element(By.ID,"username")
username.clear()
username.send_keys("B191081")
pswd = driver.find_element(By.ID,"password")
pswd.clear()
pswd.send_keys("Ravi*jyothi1")
#overlay = driver.find_element(By.TAG_NAME,"b")
wait = WebDriverWait(driver, 20)
#wait.until(ec.invisibility_of_element_located((By.TAG_NAME,"b")))
#login = wait.until(ec.element_to_be_clickable((By.XPATH,"//*[@id='loginbtn']")))
login = driver.find_element(By.XPATH,"//*[@id='loginbtn']")
driver.execute_script("arguments[0].click();",login)

#functions

def save_changes():
  status = driver.find_element(By.CSS_SELECTOR,".statuscol a")
  driver.execute_script("arguments[0].click();",status)
  present = driver.find_elements(By.CLASS_NAME,"form-check-input")
  driver.execute_script("arguments[0].click();",present[0])
  submit = driver.find_element(By.ID,"id_submitbutton")
  driver.execute_script("arguments[0].click();",submit)
  
def dashboard_home():
  dashboard = driver.find_element(By.XPATH,"//*[@id='page-navbar']/nav/ol/li[1]/a")
  driver.execute_script("arguments[0].click();",dashboard)  

  
  
def send_msg():
  subject_name = driver.find_element(By.TAG_NAME,"h1").text
  msg = EmailMessage()
  msg.set_content(f"\nHey @Deva ( ^ ^ )\n\nAttendance was submitted\n\nDetails:\nSubject:{subject_name}:)\nStatus:present\n\nThank you........&&831!!!")
  msg['subject'] = "Your attendance result :)"
  msg['from'] = "attendence.result.bot@gmail.com"
  msg['to'] = "devaagulla770@gmail.com"
  server = smtplib.SMTP_SSL("smtp.gmail.com",465)
  server.login("attendence.result.bot@gmail.com","DevarajAgulla")
  server.send_message(msg)
  server.quit()
  
  
def exit_code():
    driver.close()
    driver.quit()
  
  
  
def attendance():
  subjects = driver.find_elements(By.CSS_SELECTOR,".column a")
  for i  in range(0,len(subjects)):
      try:
          subs = driver.find_elements(By.CSS_SELECTOR,".column a")
          driver.execute_script("arguments[0].click();",subs[i])
          try:
              attendance = driver.find_elements(By.CSS_SELECTOR,".modtype_attendance .aalink")
              if(len(attendance) > 0):
                  attendance[0].click()
                  #title = driver.find_element(By.TAG_NAME,"h1").text
                  #print(title)
                  try:
                      save_changes()
                      send_msg()
                  except:
                      dashboard_home()
                      continue
              dashboard_home()
          except:
             dashboard_home()
      except:
          continue
      
      
def logout():
    wait = WebDriverWait(self, 20)
    toggle_one = wait.until(ec.element_to_be_clickable((By.ID,"action-menu-toggle-1")))
    toggle_one.click()
    logout = driver.find_element(By.XPATH,"//*[@id='actionmenuaction-6']")
    logout.click()
    exit_code()    
 
while True:
    attendance()
    try:
        logout()
        exit_code()
    except:
        exit_code()
    #print("finished")
    time.sleep(2000)
#login = driver.find_element(By.ID,"loginbtn")
#login.click()
#print("finished")
