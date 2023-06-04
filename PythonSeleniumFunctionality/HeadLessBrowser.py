from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select



#ChromOption
option=webdriver.ChromeOptions()
#option.add_argument("--headless")
option.add_argument("--incognito")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.roicians.com")
print(driver.title)
driver.quit()