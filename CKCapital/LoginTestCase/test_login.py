
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def test_successful_login(driver):
    
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)
    

    username = "Shubham@codesis.tech"
    password = "Shubham@123"

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)

    
    assert "funding-evaluation" in driver.current_url.lower()