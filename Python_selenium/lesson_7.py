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

"""Информация о продукте №1."""
produkt_1 = driver_g.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор название продукта №1.
value_produkt_1 = produkt_1.text
print(f"Название продукта: {value_produkt_1}")

price_produkt_1 = driver_g.find_element(By.XPATH, "//div[@class = 'inventory_item_price']")    # Присваиваем переменной локатор цену продукта №1.
price_value_produkt_1 = price_produkt_1.text
print(f"Цена продукта: {price_value_produkt_1}")

add_to_cart = driver_g.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")    # Присваиваем переменной локатор кнопки "add to card".
add_to_cart.click()
print("Нажата кнопка 'ADD TO CARD'")

container = driver_g.find_element(By.XPATH, "//span[@class ='shopping_cart_badge']")    # Присваиваем переменной локатор кнопки "значка количесво товаров в каорзине".
value_container = container.text
print(f"Количество добавленного товара в корзину: {value_container}")

shopping_cart = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")    # Присваиваем переменной локатор кнопки "значка корзины".
shopping_cart.click()
print("Нажата кнопка 'Корзина'")

url_card = "https://www.saucedemo.com/cart.html"
get_url_card = driver_g.current_url
print(get_url_card)
assert url_card == get_url_card
print(f"Current URL: {get_url_card} matches {url_card}")

"""Информация о продукте в карзине."""
card_price_produkt_1 = driver_g.find_element(By.XPATH, "//div[@class = 'inventory_item_price']")    # Присваиваем переменной локатор цену продукта №1.
price_value_card_produkt_1 = card_price_produkt_1.text
print(f"Цена продукта в корзине: {price_value_card_produkt_1}")

"""Информация о продукте в корзине ."""
card_produkt_1 = driver_g.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор название продукта №1.
card_value_produkt_1 = card_produkt_1.text
print(f"Название продукта в корзине: {card_value_produkt_1}")
assert card_value_produkt_1 == value_produkt_1
print("Название выбранного товара совпадает с названием в корзине")

card_produkt_1 = driver_g.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор название продукта №1.
card_value_produkt_1 = card_produkt_1.text
print(f"Цена продукта в корзине: {card_value_produkt_1}")
assert card_value_produkt_1 == value_produkt_1
print("Цена выбранного товара совпадает с ценой в корзине")