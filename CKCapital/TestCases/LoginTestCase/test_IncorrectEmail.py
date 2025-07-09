
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Incorrect_Email(driver):

    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)
    

    username = "Shubhamm@codesis.tech"
    password = "Shubham@123"

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)


    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='User not registered.']"))
    ).text

    print("Error Message:", error_message)

    
    assert "user not registered" in error_message.lower()