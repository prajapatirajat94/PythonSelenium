from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



browserName='firefox'


if browserName=='chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName=='firefox':
    driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please enter correct browser name: .....")
    raise Exception("no browser found")

driver.implicitly_wait(5)

driver.quit()


