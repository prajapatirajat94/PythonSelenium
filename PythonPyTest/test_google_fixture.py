import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

#To generate html report :-  python -m pytest test_google_test.py -v -s --html=google_report.html

driver = None
#below method will run initially
@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
@pytest.mark.title # we can use marker combination
def test_googletitle(init_driver): #here we are writing fixture name inside method or you can use @pytest.mark.usefixtures("fixturename")
    assert driver.title=="Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url(init_driver):
    time.sleep(2)
    assert driver.current_url=="https://www.google.com/"
    time.sleep(2)
