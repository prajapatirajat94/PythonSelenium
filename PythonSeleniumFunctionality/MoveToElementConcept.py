from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.delete_cookie()
driver.get("https://www.roicians.com")
time.sleep(5)

Courses= driver.find_element(By.XPATH,'(//a[text()="Courses"])[1]')
#need to use ActionChains(driver) class to perform move to element operation
action_chain=ActionChains(driver)
action_chain.move_to_element(Courses).perform()
time.sleep(3)
Software_Testing=driver.find_element(By.XPATH,'(//a[text()="SOFTWARE TESTING"])[1]')
Software_Testing.click()
time.sleep(3)
Services=driver.find_element(By.XPATH,'(//a[text()="Services"])[1]')
action_chain.move_to_element(Services).perform()


#below method is for drag and drop
#action_chain.drag_and_drop("Source element","TargetElement")
#action_chain.click_and_hold("Source").move_to_element("Target").release().perform()
time.sleep(3)
print(driver.title)



