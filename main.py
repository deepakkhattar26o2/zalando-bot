from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
s = Service(r'E:\geckodriver.exe')
driver = webdriver.Firefox(service=s)
load_dotenv()
username = os.getenv('uname')
pswd = os.getenv('pswd')
driver.get('https://en.zalando.de/login/')
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'login.email'))
)
driver.find_element(By.ID, 'login.email').send_keys('61333c@libero.it')
driver.find_element(By.ID, 'login.secret').send_keys('cb40903333')
driver.find_element(By.XPATH, '//button[@aria-label="Login"]').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@data-testid="login_error_notification"]'))
    )
except:
    print('Logged In Successfully')


try:
    driver.get(
        'https://en.zalando.de/new-balance-ws327-trainers-dark-violetglow-ne211a0kd-t11.html?_rfl=de')
except:
    print('Error in Opening Site')

print('DEVLOG Product Page Reached!')

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[@id="uc-btn-accept-banner"]'))
    )
except:
    print('Button Not Found Timed Out')

driver.find_element(By.XPATH, '//button[@id="uc-btn-accept-banner"]').click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[@id="picker-trigger"]'))
    )
except:
    print('Button Not Found Timed Out')

try:
    driver.find_element(By.XPATH, '//button[@id="picker-trigger"]').click()
except:
    print('List Clicker Didn\'t Work')

print('DEVLOG List Opened')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//label[contains(@for, "size-picker-")]'))
    )
except:
    print('Label Not Found Timed Out')

shoe_list = driver.find_elements(
    By.XPATH, '//label[contains(@for, "size-picker-")]')
print('Length of List : ', len(shoe_list))
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Notify Me']"))
    )
except:
    print('Span Not Found TImed Out')
for i in shoe_list:
    try:
        i.find_element(By.XPATH, ".//span[text()='Notify Me']")
        print('unavailable shoe')
    except:
        i.click()
        break
driver.find_element(By.XPATH, '//button[@aria-label="Add to bag"]').click()
