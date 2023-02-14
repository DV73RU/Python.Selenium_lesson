import datetime
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')
options.add_argument('--mute-audio')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-infobars')
options.add_argument('--no-sandbox')
options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-breakpad')

g = Service('H:\Python.Selenium_lesson-1\Python_selenium\chromedriver.exe')
driver_g: WebDriver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

login = "standard_user"
password_all = "secret_sauce"

user_name = driver_g.find_element(By.ID, 'user-name')
user_name.send_keys(login)
password = driver_g.find_element(By.ID, 'password')
password.send_keys(password_all)
button_login = driver_g.find_element(By.ID, 'login-button')
button_login.click()

menu = driver_g.find_element(By.XPATH, "//button[@id ='react-burger-menu-btn']")
menu.click()
link_abaut = driver_g.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
ActionChains(driver_g).move_to_element(link_abaut).click().perform()

url_about = "https://saucelabs.com/"
get_url_about = driver_g.current_url
assert url_about == get_url_about
print(f"Current URL: {get_url_about} matches {url_about}")
