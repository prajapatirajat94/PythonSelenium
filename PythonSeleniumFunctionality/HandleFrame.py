from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.delete_cookie()
driver.implicitly_wait(10)
driver.get("")

#change frame
driver.switch_to.frame(2)
driver.switch_to.frame("name or ID")
#driver.switch_to.frame(WebElementss)
#driver.switch_to.parent_frame()
#https://the-internet.herokuapp.com/basic_auth