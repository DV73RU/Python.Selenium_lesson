"""Очистка содержимого."""

import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

login = "standard_user"
password_all = "secret_sauce"

user_name = driver_g.find_element(By.ID, 'user-name')
user_name.send_keys(login)
print('Ввод логин')
time.sleep(2)

password = driver_g.find_element(By.ID, 'password')
password.send_keys(password_all)
print('Ввод пароля')
time.sleep(2)

button_login = driver_g.find_element(By.ID, 'login-button')
button_login.click()
print('Клик')

time.sleep(2)

