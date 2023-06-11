from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)

driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(3)

#To send value in elements
JavaSearchGoogle = "document.getElementById('APjFqb').value='Rajat';"
driver.execute_script(JavaSearchGoogle)
#Below methos is to highlight element
#driver.execute_script("arguments[0].style.border = '3px solid red'",JavaSearchGoogle)

time.sleep(3)

print(driver.execute_script("return document.title;"))

#To get inner Text
innertext=driver.execute_script("return document.documentElement.innerText;")
print(innertext)

#To click on element
aboutbutton =driver.find_element(By.XPATH,"//a[text()='About']")
driver.execute_script("arguments[0].click();",aboutbutton)

#scroll up or down
#driver.execute_script("window.scrollBy(0,1000)")

#Scroll to view element
driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element(By.XPATH,"//a[@data-g-cta_text='Get product support']"))
#To scroll till bottom of the page
time.sleep(2)
driver.execute_script("window.scrollBy(0,-1000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)



#Other Way
# javas = "document.getElementsByName('user-search')[0].click();"
# driver.execute_script(javas)
