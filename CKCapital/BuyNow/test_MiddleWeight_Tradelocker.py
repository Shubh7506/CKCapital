
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# MiddleWeight > Tradelocker > $61
def test_middle61(default_login):
    
    driver = default_login

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()
    
    Buy_now = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='88.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$88.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "15" in driver.current_url.lower()

    assert price_element.text.strip() == "$88.00"

    assert Challenge_element.text.strip() == "5000"


    time.sleep(3)
    
    driver.quit()


# # MiddleWeight > Tradelocker > $89
def test_middle89(default_login):

    driver = default_login  

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='128.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_middle_wrapper']//div//p[@class='value'][normalize-space()='$128.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "14" in driver.current_url.lower()

    assert price_element.text.strip() == "$128.00"

    assert Challenge_element.text.strip() == "10000"


    time.sleep(3)
    
    driver.quit()


# MiddleWeight > Tradelocker > $159
def test_middle159(default_login):

    driver = default_login  

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='228.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_middle_wrapper']//div//p[@class='value'][normalize-space()='$228.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "16" in driver.current_url.lower()

    assert price_element.text.strip() == "$228.00"

    assert Challenge_element.text.strip() == "25000"


    time.sleep(3)
    
    driver.quit()


# MiddleWeight > Tradelocker > $229
def test_middle229(default_login):

    driver = default_login  

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()
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
    
    assert "17" in driver.current_url.lower()

    assert price_element.text.strip() == "$328.00"

    assert Challenge_element.text.strip() == "50000"


    time.sleep(3)
    
    driver.quit()


# MiddleWeight > Tradelocker > $369
def test_middle369(default_login):

    driver = default_login  

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()

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
    
    assert "18" in driver.current_url.lower()

    assert price_element.text.strip() == "$528.00"

    assert Challenge_element.text.strip() == "100000"


    time.sleep(3)
    
    driver.quit()


# MiddleWeight > Tradelocker > $761
def test_middle761(default_login):

    driver = default_login  

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()

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
    
    assert "19" in driver.current_url.lower()

    assert price_element.text.strip() == "$1088.00"

    assert Challenge_element.text.strip() == "200000"


    time.sleep(3)
    
    driver.quit()


# MiddleWeight > Tradelocker > $1181
def test_middle1181(default_login):

    driver = default_login  
    time.sleep(3)

    Middle_Weight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Middleweight']")))
    
    Middle_Weight.click()

    Buy_now1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strike[normalize-space()='1688.00']")))
    
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_lower_top_wrapper']//div//p[@class='value'][normalize-space()='$1688.00']")))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", price_element)
    
    assert "20" in driver.current_url.lower()

    assert price_element.text.strip() == "$1688.00"

    assert Challenge_element.text.strip() == "300000"


    time.sleep(3)
    
    driver.quit()