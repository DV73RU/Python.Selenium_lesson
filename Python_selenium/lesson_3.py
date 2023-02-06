import time
import datetime
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

login = "standard_user"
password_all = "secret_sauce"
user_name = driver_g.find_element(By.ID, 'user-name')
user_name.send_keys(login)
print('Ввод логин')
password = driver_g.find_element(By.ID, 'password')
password.send_keys(password_all)
print('Ввод парол')
button_login = driver_g.find_element(By.ID, 'login-button')
button_login.click()
print('Клик')
text_produkts = driver_g.find_element(By.XPATH, '//*[@class="title"]')
value_test_preoduction = text_produkts.text
assert value_test_preoduction == "PRODUCTS"
print("Тест не авторизации пройден")

url = "https://www.saucedemo.com/inventory.html"
get_url = driver_g.current_url
print(get_url)
assert url == get_url
print("Url: " + url + " главной корректный")
time.sleep(2)
new_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")    # Время создания скриншёта.
name_skrin = 'skr_' + new_data + '.png'     # Генерируем имя файла скриншёта.
driver_g.save_screenshot('H:\\Python.Selenium_lesson-1\\Python_selenium\\screen\\' + name_skrin)    # Создаём сриншёт в папке screen

# time.sleep(10)
# driver_g.close()
