# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()
user_name = driver_g.find_element(By.ID, 'user_name')
user_name.send_keys('standard_user')


# time.sleep(10)
# driver_g.close()
