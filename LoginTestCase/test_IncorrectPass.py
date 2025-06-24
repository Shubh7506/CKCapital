import driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Incorrect_pass(driver):
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    username = "Shubham@codesis.tech"
    password = "Shubhamaa@123"

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)


    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='INVALID_PASSWORD']"))
    ).text

    print("Error Message:", error_message)

    
    assert "INVALID_PASSWORD" in error_message.upper()