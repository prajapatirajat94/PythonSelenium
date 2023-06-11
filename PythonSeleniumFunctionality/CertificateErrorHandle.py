from selenium import  webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



option=webdriver.ChromeOptions()
#1st Way
#below 2 arguments we need to add for to ignorre certificate - This one is for chrome
# option.add_argument("--allow-running-insecure-content")
# option.add_argument("--ignore-certificate-errors")
#2ndway:
desired_compabaility=DesiredCapabilities().CHROME.copy()
desired_compabaility['acceptInsecureCerts']=True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)



driver.maximize_window()

driver.get("https://expired.badssl.com/")

s=driver.find_element(By.TAG_NAME,"h1").text
time.sleep(2)
print(s)