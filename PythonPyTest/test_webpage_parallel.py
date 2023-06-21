import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

#To run prallel test first need to install one package:- pip install pytest-xdist
# run command -> python -m pytest test_webpage.py -n 4


def test_Google1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    time.sleep(2)
    assert driver.title == "Google"
    time.sleep(2)
    driver.quit()

def test_Google2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    time.sleep(2)
    assert driver.title == "Google"
    time.sleep(2)
    driver.quit()

def test_Google3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    time.sleep(2)
    assert driver.title == "Google"
    time.sleep(2)
    driver.quit()
