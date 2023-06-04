from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select



option=webdriver.ChromeOptions()
option.add_argument("--headless")
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)

driver.get("https://www.torontopubliclibrary.ca/using-the-library/your-library-card/")

#use below method to take screenshot
#driver.get_screenshot_as_file('torontoLIb.png')

#take full screenshot - make sure you are running in headless mode
S=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('fullscrennshott.png')
print(driver.title)