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

login = "standard_user1"
password_all = "secret_sauce"
url = "https://www.saucedemo.com/"
get_url = driver_g.current_url
print(get_url)
assert url == get_url
print("Url: " + url + " главной корректный")
user_name = driver_g.find_element(By.ID, 'user-name')
user_name.send_keys(login)
print('Ввод логин')
password = driver_g.find_element(By.ID, 'password')
password.send_keys(password_all)
print('Ввод парол')
button_login = driver_g.find_element(By.ID, 'login-button')
button_login.click()
print('Клик')


warning_text = driver_g.find_element(By.XPATH, "//H3[@data-test='error']")
value_warnind_text = warning_text.text
assert value_warnind_text == "Epic sadface: Username and password do not match any user in this service"

print("GOOD TEST")
# if value_test_preoduction == "PRODUCTS":
#     print("Тест авторизации пройден")
# else:
#     print("Тест не авторизации не пройден")

# time.sleep(10)
# driver_g.close()



