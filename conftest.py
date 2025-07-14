
import pytest
import time

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from CKCapital.utils.screenshot import attach_screenshot_to_report




@pytest.fixture
def default_login(request):
    
   

    driver = webdriver.Chrome()
    

    driver.maximize_window()

    # Attach the driver to the request for access in hooks
    request.node.driver = driver

    login_url = "https://app.ckcapital.co.uk/signin"
    driver.get(login_url)

    username = "shubham@codesis.io"
    password = "Testinng@123"

    username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
    
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".signinform-button.standard_button")

    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)

    
    assert "funding-evaluation" in driver.current_url.lower()
    yield driver
    driver.quit()


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    request.node.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        attach_screenshot_to_report(item, rep)
    
    







