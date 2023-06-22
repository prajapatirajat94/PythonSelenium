import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

# 1st Step :- >
@pytest.fixture(scope="class")
def init_chrome_driver(request):

    ch_driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #below means at class level we are accessing driver
    request.cls.driver=ch_driver
    yield
    ch_driver.close()

#2nd Step : - >
@pytest.mark.usefixtures("init_chrome_driver")
class Base_chrome_Test:
    pass

#This class extend base test
class Test_Google_Chrome(Base_chrome_Test):

    def test_google_chrome_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"







