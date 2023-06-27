import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

#This code we have written in confitest.py file
# @pytest.fixture(params=["chrome","firefox"],scope="class")
# def init_driver(request):
#     if request.param=="chrome":
#         web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))
#     request.cls.driver=web_driver
#     yield
#     web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        time.sleep(5)
        assert self.driver.title == "Google"

    def test_google_url(self):
        time.sleep(2)
        assert self.driver.current_url == "https://www.google.com/"
        time.sleep(2)