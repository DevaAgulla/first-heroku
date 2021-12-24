import os
from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#import time

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
'''while True:
  try:
    login.click()
    print("worked")
    break
  except:
    print("fucked up")
    continue'''
#login = driver.find_element(By.ID,"loginbtn")
#login.click()
print("finished")
