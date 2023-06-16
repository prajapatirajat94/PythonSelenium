from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.orangehrm.com/")
driver.implicitly_wait(10)
driver.maximize_window()
Contact_SAles=driver.find_element(By.XPATH,"(//button[text()='Contact Sales'])[2]")
Contact_SAles.click()
time.sleep(5)
Enter_name=driver.find_element(By.XPATH,"//input[@name='FullName']")
Enter_name.send_keys("Rajatkumar")
time.sleep(2)
Enter_phone=driver.find_element(By.XPATH,"//input[@name='Contact']")
Enter_phone.send_keys("306789456")
time.sleep(20)
#use amazon website for practice
