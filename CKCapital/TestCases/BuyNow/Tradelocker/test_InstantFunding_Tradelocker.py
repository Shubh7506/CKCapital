
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Instant Funding > Tradelocker > $75
def test_instant5k(default_login):
    
    driver = default_login

    Instant_Funding = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Instant Funding']")))
    
    Instant_Funding.click()
    
    Buy_now = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='108.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Buy_now)

    time.sleep(2)

    Buy_now.click()

#For Challenge verification
    Challenge_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='challange-amount-options active_option']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Challenge_element)
    

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

#For Price verification
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$108.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "29" in driver.current_url.lower()

    assert price_element.text.strip() == "$108.00"

    assert Challenge_element.text.strip() == "5000"


    time.sleep(3)
    
    driver.quit()


#  Instant Funding > Tradelocker > $103
def test_instant10k(default_login):

    driver = default_login  

    Instant_Funding = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Instant Funding']")))
    
    Instant_Funding.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='148.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Buy_now1)

    time.sleep(2)

    Buy_now1.click()

#For Challenge verification
    Challenge_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='challange-amount-options active_option']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Challenge_element)
    

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

#For Price verification
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$148.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "30" in driver.current_url.lower()

    assert price_element.text.strip() == "$148.00"

    assert Challenge_element.text.strip() == "10000"


    time.sleep(3)
    
    driver.quit()


#  Instant Funding > Tradelocker > $180
def test_instant25k(default_login):

    driver = default_login  

    Instant_Funding = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Instant Funding']")))
    
    Instant_Funding.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='258.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Buy_now1)

    time.sleep(2)

    Buy_now1.click()

    #For Challenge verification
    Challenge_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='challange-amount-options active_option']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Challenge_element)
    

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

#For Price verification
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$258.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "31" in driver.current_url.lower()

    assert price_element.text.strip() == "$258.00"

    assert Challenge_element.text.strip() == "25000"


    time.sleep(3)
    
    driver.quit()


#  Instant Funding > Tradelocker > $548
def test_instant50k(default_login):

    driver = default_login  

    Instant_Funding = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Instant Funding']")))
    
    Instant_Funding.click()
    time.sleep(3)

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='548.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Buy_now1)

    time.sleep(2)

    Buy_now1.click()

    #For Challenge verification
    Challenge_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='challange-amount-options active_option']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Challenge_element)
    

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

#For Price verification
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$548.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "32" in driver.current_url.lower()

    assert price_element.text.strip() == "$548.00"

    assert Challenge_element.text.strip() == "50000"


    time.sleep(3)
    
    driver.quit()


