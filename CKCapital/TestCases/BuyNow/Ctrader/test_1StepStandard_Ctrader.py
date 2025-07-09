
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 1 Step Standard > Ctrader > $159
def test_step25k(default_login):
    
    driver = default_login

    Step_Standard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='1 Step Standard']")))
    
    Step_Standard.click()

    Ctrader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CTRADER']")))
    
    Ctrader.click()
    
    Buy_now = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='228.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$228.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "25" in driver.current_url.lower()

    assert price_element.text.strip() == "$228.00"

    assert Challenge_element.text.strip() == "25000"


    time.sleep(3)
    
    driver.quit()





#  1 Step Standard> Tradelocker > $229
def test_step50k(default_login):

    driver = default_login  

    Step_Standard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='1 Step Standard']")))
    
    Step_Standard.click()

    Ctrader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CTRADER']")))
    
    Ctrader.click()
    time.sleep(3)

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='328.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$328.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "26" in driver.current_url.lower()

    assert price_element.text.strip() == "$328.00"

    assert Challenge_element.text.strip() == "50000"


    time.sleep(3)
    
    driver.quit()


#  1 Step Standard > Ctrader > $369
def test_step100k(default_login):

    driver = default_login  

    Step_Standard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='1 Step Standard']")))
    
    Step_Standard.click()

    Ctrader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CTRADER']")))
    
    Ctrader.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='528.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$528.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "27" in driver.current_url.lower()

    assert price_element.text.strip() == "$528.00"

    assert Challenge_element.text.strip() == "100000"


    time.sleep(3)
    
    driver.quit()


#  1 Step Standard > Ctrader > $761
def test_step200k(default_login):

    driver = default_login  

    Step_Standard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='1 Step Standard']")))
    
    Step_Standard.click()

    Ctrader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='CTRADER']")))
    
    Ctrader.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='1088.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$1088.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "28" in driver.current_url.lower()

    assert price_element.text.strip() == "$1088.00"

    assert Challenge_element.text.strip() == "200000"


    time.sleep(3)
    
    driver.quit()


