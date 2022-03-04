import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as wd

options = {
'proxy': {
    'http': 'http://mr7081aCjw:Mw7qvE1CMO@ultra.marsproxies.com:12323',
    'https':'https://mr7081aCjw:Mw7qvE1CMO@ultra.marsproxies.com:12323',
    'no_proxy': 'localhost,127.0.0.1,dev_server:8080'
    }
}

s = Service(r'E:\geckodriver.exe')
file = open('listo.csv')
filename = 'res.csv'
csvreader = csv.reader(file)
header = []
header = next(csvreader)
# def driver.close():
#     try : 
#         driver.get('https://en.zalando.de/logout/')
#     except:
#         print('uh oh!')
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['Email','Password','LOGIN_STATUS','CART_STATUS'])
    for row in csvreader :
        driver = wd.Firefox(service = s, seleniumwire_options=options)
        driver.get('https://en.zalando.de/')
        try:
            driver.get('https://en.zalando.de/login/')
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, 'login.email'))
            )
            # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.find_element(By.ID, 'login.email').send_keys(row[0].strip())
            driver.find_element(By.ID, 'login.secret').send_keys(row[1].strip())
            driver.find_element(By.XPATH, '//button[@aria-label="Login"]').click()
        except : 
            print('DEVLOG Login Process Failed', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'Fail', 'Fail'])
            driver.close()
            continue
        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@data-testid="login_error_notification"]'))
            )
            print('Login Failed', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'FAIL', 'FAIL'])
            driver.close()
            continue
        except:
            print('DEVLOG Logged In Successfully')

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@id="uc-btn-accept-banner"]'))
            )
            print('Hover Button Found ehehe')
        except:
            print('DEVLOG Button Not Found Timed Out', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue
        try:
            driver.find_element(By.XPATH, '//button[@id="uc-btn-accept-banner"]').click()
            print('DEVLOG Hover Button Click Worked haha')
        except:
            print('DEVLOG Hover Button Click Didn\'t Work')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue


        try:
            driver.get(
                'https://en.zalando.de/new-balance-ws327-trainers-dark-violetglow-ne211a0kd-t11.html?_rfl=de')
        except:
            print('DEVLOG Error in Opening Product Page')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        print('DEVLOG Product Page Reached!')

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@id="picker-trigger"]'))
            )
        except:
            print('DEVLOG Button Not Found Timed Out')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        try:
            driver.find_element(By.XPATH, '//button[@id="picker-trigger"]').click()
        except:
            print('DEVLOG List Clicker Didn\'t Work')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        print('DEVLOG List Opened')

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//label[contains(@for, "size-picker-")]'))
            )
        except:
            print('DEVLOG Label Not Found Timed Out')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        shoe_list = driver.find_elements(
            By.XPATH, '//label[contains(@for, "size-picker-")]')
        print('DEVLOG Length of List : ', len(shoe_list))

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[text()='Notify Me']"))
            )
        except:
            print('DEVLOG Span Not Found TImed Out')
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue
        for i in shoe_list:
            try:
                i.find_element(By.XPATH, ".//span[text()='Notify Me']")
                print('DEVLOG unavailable shoe')
            except:
                i.click()
                break

        try:
            driver.find_element(By.XPATH, '//button[@aria-label="Add to bag"]').click()
            print('DEVLOG Add to Bag Clicked')
        except  :
            print('DEVLOG Add to Bag Failed', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        try:
            driver.get(
                'https://en.zalando.de/cart/')
        except:
            print('DEVLOG Error in Opening Cart Page', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue

        print('DEVLOG Cart Page Reached!')

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h4[@class='z-2-text z-coast-base__article__name z-2-text-body-small-regular z-2-text-gray' and  text()='WS327 - Trainers - dark violet/glow']"))
            )
            print('DEVLOG Shoe Found In Cart', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'PASS'])
            driver.close()
            continue
        except:
            print('DEVLOG Shoe Not Found in Cart', row[0].strip())
            csvwriter.writerow([row[0].strip(), row[1].strip(), 'PASS', 'FAIL'])
            driver.close()
            continue
file.close()
# driver.quit()
#//h2[text()='Your bag']
#//div[@class="z-coast-fjord-miniCart_articleProductName" and text()='KENT COLLAR LONG SLEEVE - Shirt - stormy sea']