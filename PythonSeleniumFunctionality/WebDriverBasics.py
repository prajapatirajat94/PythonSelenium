from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#first import :- from selenium import webdriver

#service_obj=Service("/chromedriver")
driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.find_element(By.NAME,'q').send_keys('naveen auto')
driver.implicitly_wait(10)
print(driver.title)
time.sleep(2)
optionlist = driver.find_elements(By.XPATH,'//div[@class="wM6W7d"]//span')
print(len(optionlist))

for x in optionlist:

    clickonoption= x.text
    if x.text =='naveen automationlabs youtube':
        x.click()
        break

time.sleep(6)

driver.quit()
