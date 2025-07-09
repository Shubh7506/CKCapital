
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Without_Pass(driver):

    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)
    

    username = "Shubham@codesis.tech"
    

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    
    login_button.click()
    time.sleep(5)


    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
    ).text

    print("Error Message:", error_message)

    
    expected_message = "Password is required"

    assert expected_message.lower() in error_message.lower()