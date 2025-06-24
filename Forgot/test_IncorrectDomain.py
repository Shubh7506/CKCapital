import driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Incorrect_Domain(driver):
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    

    forgot_pass = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Forgot Password ?']")))
    
    forgot_pass.click()

    time.sleep(3)
    
    Email = "Shubham@codesis.i"
    

    forgot_pass_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
    
    forgot_pass_field.send_keys(Email)

    Submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")

    Submit_button.click()

    time.sleep(5)


    
    


    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='error_modal_container_bottom'] p"))
    ).text

    print("Error Message:", error_message)

    expected_message = "Please check the email !"

    assert expected_message.lower() in error_message.lower()