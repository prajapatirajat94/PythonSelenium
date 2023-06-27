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


@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass

class Test_sauce(BaseTest):


    @pytest.mark.parametrize("username,password",[("Rajat","Rsting@123"),("Kajol","Rsting123"),
                                                  ("Kajol","Rsting123")])
    def test_parameter(self,username,password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)


