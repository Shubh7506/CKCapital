
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Numeric_Email(driver):

    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)
    

    
    password = "Shubham@123"

    
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)


    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
    ).text

    print("Error Message:", error_message)

    
    expected_message = "Email is required"

    assert expected_message.lower() in error_message.lower()