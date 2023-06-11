from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.orangehrm.com/en/contact-sales/")


ele_Country=driver.find_element(By.XPATH,"//select[@name='Country']")
#we have to import select class
Coutry_SELECT=Select(ele_Country)
Coutry_SELECT.select_by_index(5)
time.sleep(3)
Coutry_SELECT.select_by_visible_text("India")
time.sleep(3)
Coutry_SELECT.select_by_value("Canada")
time.sleep(3)

ALLCountry=Coutry_SELECT.options
for x in ALLCountry:
    print(x.text)



time.sleep(5)
Emloyee_select=driver.find_element(By.XPATH,"//select[@name='NoOfEmployees']")
EMP_SELECT_VAL=Select(Emloyee_select)
EMP_SELECT_VAL.select_by_index(5)
EMP_VAl=EMP_SELECT_VAL.options
for y in EMP_VAl:
    print(y.text)
time.sleep(3)