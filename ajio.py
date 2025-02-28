import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


drive = Service("C:/Users/sadat/OneDrive/Desktop/chromedriver.exe")
#chrome_options=Options()
#chrome_options.add_experimental_option("detach",True)
#chrome_options.add_experimental_option('excludesSwitches',['enable-logging'])
#chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--ignore-ssl-errors')
#chrome_options.add_argument("start-maximized")
driver=uc.Chrome(service=drive)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:


    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height



html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)