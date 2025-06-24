import pytest
import pytest_check as check

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup_field(driver):
    
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    time.sleep(2)
    

    

    signup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sign Up')]")))
    
    signup.click()

    time.sleep(3)
    
    

    Submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']")

    Submit_button.click()

    time.sleep(5)


    
    


    first_name_error = driver.find_element(By.XPATH, "//div[contains(text(),'First Name is required')]").text
    last_name_error = driver.find_element(By.XPATH, "//div[contains(text(),'Last Name is required')]").text
    contact_error = driver.find_element(By.XPATH, "//div[contains(text(),'Number is required')]").text
    email_error = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required')]").text
    confirm_email_error = driver.find_element(By.XPATH, "//div[contains(text(),'Confirm Email is required')]").text
    city_error = driver.find_element(By.XPATH, "//div[contains(text(),'City is required')]").text
    password_error = driver.find_element(By.XPATH, "//div[contains(text(),'Password is required')]").text


    assert last_name_error.strip() == "Last Name is required"
    assert first_name_error.strip() == "First Name is required"
    assert contact_error.strip() == "Number is required"
    assert email_error.strip() == "Email is required"
    assert confirm_email_error.strip() == "Confirm Email is required"
    assert city_error.strip() == "City is required"
    assert password_error.strip() == "Password is required"
    

    time.sleep(3)

    driver.quit()