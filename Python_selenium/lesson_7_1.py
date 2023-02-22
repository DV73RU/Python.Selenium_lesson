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

"""Информация о продукте №1 на странице."""
produkt_1 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")       # Присваиваем переменной локатор название продукта №1 на странице.
value_produkt_1 = produkt_1.text
print(f"Название продукта: {value_produkt_1}")

# Присваиваем переменной локатор цену продукта №1.
price_produkt_1 = driver_g.find_element(
    By.XPATH, "//div[@class = 'inventory_item_price']")
price_value_produkt_1 = price_produkt_1.text
print(f"Цена продукта: {price_value_produkt_1}")

# Присваиваем переменной локатор кнопки "add to card".
add_to_cart = driver_g.find_element(
    By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
add_to_cart.click()
print("Нажата кнопка 'ADD TO CARD'")

# Присваиваем переменной локатор кнопки "значка количесво товаров в каорзине".
container = driver_g.find_element(
    By.XPATH, "//span[@class ='shopping_cart_badge']")
value_container = container.text
print(f"Количество добавленного товара в корзину: {value_container}")

# Присваиваем переменной локатор кнопки "значка корзины".
shopping_cart = driver_g.find_element(
    By.XPATH, "//a[@class='shopping_cart_link']")
shopping_cart.click()
print("Нажата кнопка 'Корзина'")


"""Проверяем что открыта страница корзины"""
url_card = "https://www.saucedemo.com/cart.html"
get_url_card = driver_g.current_url
print(get_url_card)
assert url_card == get_url_card
# Выводим сообщение о коректности url корзины.
print(f"Current URL: {get_url_card} matches {url_card}")

"""Информация о продукте в корзине."""
card_produkt_1 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор цену продукта №1 в корзине.
card_value_produkt_1 = card_produkt_1.text
print(f"Название продукта в корзине: {card_value_produkt_1}")
assert value_produkt_1 == card_value_produkt_1
print("Название продукта на странице одинковое с названием продукта в корзине.")

"""Информация о цене продукта в корзине ."""
card_prise_produkt_1 = driver_g.find_element(
    By.XPATH, "//div[@class = 'inventory_item_price']")    # Присваиваем переменной локатор название продукта №1.
card_prise_value_produkt_1 = card_prise_produkt_1.text
print(f"Цена продукта в корзине: {card_prise_value_produkt_1}")
assert price_value_produkt_1 == card_prise_value_produkt_1
print("Цена продукта на странице одинаковая с ценой продукта в корзине.")

button_checkout = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
button_checkout.click()
print('Клик кнопку "checkout"')
time.sleep(2)

"""Проверяем что открыта страница формы заполнения"""
url_info = "https://www.saucedemo.com/checkout-step-one.html"
get_url_info = driver_g.current_url
print(get_url_info)
assert url_info == get_url_info
print(f"Current URL: {get_url_info} matches {url_info}")

"""Заполнение форму о пользователе."""

first = "Dmitriy"
last = "Barsukov"
code = "433734"

first_name = driver_g.find_element(By.XPATH, "//input[@id = 'first-name']")
first_name.send_keys(first)
print(f"Введено в поле first name: {first}")
time.sleep(2)

last_name = driver_g.find_element(By.XPATH, "//input[@id = 'last-name']")
last_name.send_keys(last)
print(f"Введено в поле last_name: {last}")
time.sleep(2)

postal_code = driver_g.find_element(By.XPATH, "//input[@id = 'postal-code']")
postal_code.send_keys(code)
print(f"Ввдено в поле postal code: {code}")
time.sleep(2)

button_continue = driver_g.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Клик на кнопку "Continue"')
time.sleep(2)

"""Информация на странице OVERVIEW."""

# Присваиваем переменной локатор название продукта №1 в ovarview.
ovarview_produkt_1 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")
ovarview_value_produkt_1 = ovarview_produkt_1.text
print(f"Название продукта на странице OVERVIEW: {ovarview_value_produkt_1}")
# Проверяем равенство переменных(цены) корзины и на странице ovarview.
assert ovarview_value_produkt_1 == card_value_produkt_1
print("Название продукта в корзине одинковое с названием продукта странеце OVERVIEW.")

"""Информация о цене продукта в OVERVIEW."""
ovarview_prise_produkt_1 = driver_g.find_element(
    By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")    # Присваиваем переменной локатор цены продукта №1 в ovarview.
ovarview_prise_value_produkt_1 = ovarview_prise_produkt_1.text
print(f"Цена продукта на странице OVERVIEW: {ovarview_prise_value_produkt_1}")


"""Информация о цене продукта в Item total."""
sammary_prise_1 = driver_g.find_element(
    By.XPATH, "//div[@class = 'summary_subtotal_label']")   # Присваиваем переменной локатор цену продукта №1 в Item total.
sammary_prise_1 = sammary_prise_1.text
print(f"Итоговая сумма: {sammary_prise_1}")

item_total = "Item total: " + ovarview_prise_value_produkt_1
print(f"Итоговая сумма в Item total {item_total}")
assert item_total == sammary_prise_1
print(f"Сумма на странице OVERVIEW одинаковая с итоговой суммой в Item total.")