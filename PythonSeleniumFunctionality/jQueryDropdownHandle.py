from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

def SelectDropdown(Drop_List,value):
    if not value[0] =='all':
        for ele in Drop_List:
            print(ele.text)
            for K in range(len(value)):
                if ele.text==value[K]:
                    ele.click()
                    break
    else:
        try:
           for ele in Drop_List:
               ele.click()
        except Exception as e:
            print(e)



driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='justAnInputBox']").click()
time.sleep(3)



Drop_List = driver.find_elements(By.XPATH, "//ul//li/span[@class='comboTreeItemTitle']")

value_list=['all']
SelectDropdown(Drop_List,value_list)


time.sleep(2)