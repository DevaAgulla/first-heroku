import os
from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import time

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#op.add_argument("-remote-debugging-port=9224")
op.add_argument("--headless")
op.add_argument("--disable-dev-sh-usage")
op.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
driver.get("http://lms.rgukt.ac.in/login/index.php")
driver.implicitly_wait(30)
#login script
username = driver.find_element(By.ID,"username")
username.clear()
username.send_keys("B191081")
pswd = driver.find_element(By.ID,"password")
pswd.clear()
pswd.send_keys("Ravi*jyothi1")
login = driver.find_element(By.ID,"loginbtn")
login.click()
