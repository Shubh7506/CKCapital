import pytest
from CKCapital.utils.data_loader import load_forgot_password_cases
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_data1 = load_forgot_password_cases()

@pytest.mark.parametrize('row', test_data1)
def test_forgot(driver, row):
    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    username = row["email"]
    expected_message = row["expected_message"]

    # Wait for and click the 'Forgot Password ?' label
    forgot_pass = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Forgot Password ?']"))
    )
    forgot_pass.click()

    # Wait for and interact with the email field
    forgot_pass_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    forgot_pass_field.clear()
    forgot_pass_field.send_keys(username)

    # Wait for and click the Submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
    )
    submit_button.click()

    # Now wait for the expected result and assert
    if expected_message == "Email_sent":
        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='success_modal_container_bottom_div'] p"))
        ).text
        assert "an email has been sent" in message.lower()

    elif expected_message == "Check_email" or expected_message == "Invalid_email":
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='error_modal_container_bottom'] p"))
        ).text
        assert "please check the email" in error_message.lower()
        

    elif expected_message == "Email_is_required":
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".forgotpasswordform-error"))
        ).text
        assert "Please check the email !" in error_message.lower()
        
        



