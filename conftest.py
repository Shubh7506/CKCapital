
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging

logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)


@pytest.fixture
def default_login():
    
   

    driver = webdriver.Chrome()
    

    driver.maximize_window()

    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    username = "shubham@codesis.tech"
    password = "Unique@123"

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)

    
    assert "funding-evaluation" in driver.current_url.lower()
    yield driver



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


    
