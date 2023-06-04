from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.delete_cookie()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

Submit_Btn=driver.find_element(By.CSS_SELECTOR,"input[name='proceed']")
Submit_Btn.click()
#Alert Handling
Alert=driver.switch_to.alert
print(Alert.text)
Alert.accept()
#write below things after sending alert
driver.switch_to.default_content()
#Alert.dismiss()
#if you want alert with some text or details
#Practice Website :- https://the-internet.herokuapp.com/javascript_alerts
#Alert.send_keys("WhateverYouWantToWrite")

time.sleep(5)