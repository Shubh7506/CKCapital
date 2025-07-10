import pytest
from CKCapital.utils.data_loader import load_test_data
import json
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from CKCapital.utils.data_loader import load_test_data
# ... existing code ...

test_data = load_test_data()

@pytest.mark.parametrize("row", test_data)
def test_login(driver, row):
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    username = row["email"]
    password = row["password"]
    expected_result = row["expected_result"]

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    if expected_result == "success":
        WebDriverWait(driver, 10).until(
            EC.url_contains("funding-evaluation")
        )
        assert "funding-evaluation" in driver.current_url.lower()
    elif expected_result == "failure":
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='INVALID_PASSWORD']"))
        ).text
        assert "INVALID_PASSWORD" in error_message.upper()

    
