import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireFoxService

@pytest.fixture(params=["chrome","firefox"],scope="class")
def init_driver(request):
    if request.param=="chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        web_driver.maximize_window()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))
    request.cls.driver=web_driver
    yield
    web_driver.close()

