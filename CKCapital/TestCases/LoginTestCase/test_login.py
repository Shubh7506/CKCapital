import pytest
from CKCapital.utils.data_loader import load_test_data

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    # For valid email and password
    if expected_result == "success":
        WebDriverWait(driver, 10).until(
            EC.url_contains("funding-evaluation")
        )
        assert "fundi-evaluation" in driver.current_url.lower()
    
    # For invalid password
    elif expected_result == "failure":
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='INVALID_PASSWORD']"))
        ).text
        assert "INVAL_PASSWORD" in error_message.strip().upper()

    
    # For invalid email
    elif expected_result == "invalid_email":
        error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='User not registered.']"))
        ).text
        assert "user not registered" in error_message.strip().lower()

    # For invalid numeric email
    elif expected_result == "invalid_numeric_email":
        error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Enter a valid email address.']"))
        ).text

        print("Error Message:", error_message)

        expected_message = "Enter a valid email address."

        assert expected_message.lower().strip() in error_message.lower().strip()

    # For without email

    elif expected_result == "without_email":
        error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
        ).text

        print("Error Message:", error_message)

    
        expected_message = "Email is required"

        assert expected_message.lower().strip() in error_message.lower().strip()

    # For without password

    elif expected_result == "without_password":
        error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
        ).text

        print("Error Message:", error_message)

    
        expected_message = "Password is required"

        assert expected_message.lower().strip() in error_message.lower().strip()

    

    

    



    
