import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

driver = None
#below method will run initially - or we can use fixture
def setup_module(module):
    global driver
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

#below method will run at the end - or we can use fixture
def teardown_module(module):
    driver.quit()

def test_googletitle():
    assert driver.title=="Google"

def test_google_url():
    time.sleep(2)
    assert driver.current_url=="https://www.google.com/"
    time.sleep(2)
