"""Взаимодействие со скрытыми элементами."""

import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')
options.add_argument('--mute-audio')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-infobars')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--no-sandbox')
options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-breakpad')
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
print('Клик кнопки авторизации')
time.sleep(2)

menu = driver_g.find_element(
    By.XPATH, "//button[@id ='react-burger-menu-btn']")
menu.click()
print('Клик на кнопку меню.')
time.sleep(2)

link_abaut = driver_g.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_abaut.click()
print('Клик на кнопку About в меню.')

time.sleep(2)

url_about = "https://saucelabs.com/"
get_url_about = driver_g.current_url
print(get_url_about)
assert url_about == get_url_about
print(f"Current URL: {get_url_about} matches {url_about}")
