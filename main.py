import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
s = Service(r'E:\geckodriver.exe')
driver = webdriver.Firefox(service=s)
from dotenv import load_dotenv
load_dotenv()
username = os.getenv('uname')
pswd = os.getenv('pswd')
try : 
    driver.get('https://en.zalando.de/login/')
    # driver.find_element(By.XPATH, '//a[@title ="Login"]').click()
    element = WebDriverWait(driver, 10).until(  
            EC.presence_of_element_located((By.ID, 'login.email'))
        )
    driver.find_element(By.ID, 'login.email').send_keys('61333c@libero.it')
    driver.find_element(By.ID, 'login.secret').send_keys('cb40903333')
    driver.find_element(By.XPATH, '//button[@aria-label="Login"]').click()
    try:
        element = WebDriverWait(driver, 10).until(  
                EC.presence_of_element_located((By.XPATH, '//div[@data-testid="login_error_notification"]'))
            )   
    except : 
        print('Logged In Successfully')
    driver.get('https://en.zalando.de/new-balance-ws327-trainers-dark-violetglow-ne211a0kd-t11.html?_rfl=de')
    print('Product Page Reached!')
except : 
    driver.quit()
    print('An Error Occurred')


