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
print(f"Название продукта №1: {value_produkt_1}")

"""Информация о продукте №2 на странице."""
produkt_2 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_1_title_link']")       # Присваиваем переменной локатор название продукта №2 на странице.
value_produkt_2 = produkt_2.text
print(f"Название продукта №2: {value_produkt_2}")

# Присваиваем переменной локатор цену продукта №1.
# // TODO # Найти локатор цены  продукта №1
price_produkt_1 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
price_value_produkt_1 = price_produkt_1.text
print(f"Цена продукта №1: {price_value_produkt_1}")

# // TODO # Найти локатор цены продукта №2.
# https://www.awesomeandrew.ru/2021/08/06/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D1%83-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2-%D1%81-%D0%B8%D1%81%D0%BF/
# Присваиваем переменной локатор цену продукта №2.
price_produkt_2 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
price_value_produkt_2 = price_produkt_2.text
print(f"Цена продукта №2: {price_value_produkt_2}")

# Присваиваем переменной локатор кнопки "add to card продукта №1".
add_to_cart = driver_g.find_element(
    By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
add_to_cart.click()
print("Нажата кнопка 'ADD TO CARD' продукта №1")

# Присваиваем переменной локатор кнопки "add to card продукта №2".
add_to_cart_2 = driver_g.find_element(
    By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']")
add_to_cart_2.click()
print("Нажата кнопка 'ADD TO CARD' продукта №2")

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

time.sleep(2)
"""Информация о продукте №1 в корзине."""
card_produkt_1 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор название продукта №1 в корзине.
card_value_produkt_1 = card_produkt_1.text
print(f"Название продукта №1 в корзине: {card_value_produkt_1}")
assert value_produkt_1 == card_value_produkt_1
print("Название продукта №1 на странице одинковое с названием продукта в корзине.")

"""Информация о продукте №2 в корзине."""
card_produkt_2 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_1_title_link']")    # Присваиваем переменной локатор цену продукта №1 в корзине.
card_value_produkt_2 = card_produkt_2.text
print(f"Название продукта №2 в корзине: {card_value_produkt_2}")
assert value_produkt_2 == card_value_produkt_2
print("Название продукта №2 на странице одинковое с названием продукта в корзине.")


"""Информация о цене продукта №1 в корзине ."""
card_prise_produkt_1 = driver_g.find_element(
    By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")    # Присваиваем переменной локатор название продукта №1.
card_prise_value_produkt_1 = card_prise_produkt_1.text
print(f"Цена продукта №1 в корзине: {card_prise_value_produkt_1}")
assert price_value_produkt_1 == card_prise_value_produkt_1
print("Цена продукта №1 на странице одинаковая с ценой продукта в корзине.")

"""Информация о цене продукта №2 в корзине ."""
card_prise_produkt_2 = driver_g.find_element(
    By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")    # Присваиваем переменной локатор название продукта №1.
card_prise_value_produkt_2 = card_prise_produkt_2.text
print(f"Цена продукта №2 в корзине: {card_prise_value_produkt_2}")
assert price_value_produkt_2 == card_prise_value_produkt_2
print("Цена продукта №2 на странице одинаковая с ценой продукта в корзине.")

button_checkout = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
button_checkout.click()
print('Клик на кнопку "checkout"')
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
print(f"Введено в поле postal code: {code}")
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
print(f"Название продукта №1 на странице OVERVIEW: {ovarview_value_produkt_1}")
# Проверяем равенство переменных(цены) корзины и на странице ovarview.
assert ovarview_value_produkt_1 == card_value_produkt_1
print("Название продукта №1 в корзине одинковое с названием продукта странеце OVERVIEW.")

# Присваиваем переменной локатор название продукта №1 в ovarview.
ovarview_produkt_2 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_1_title_link']")
ovarview_value_produkt_2 = ovarview_produkt_2.text
print(f"Название продукта №2 на странице OVERVIEW: {ovarview_value_produkt_2}")
# Проверяем равенство переменных(цены) корзины и на странице ovarview.
assert ovarview_value_produkt_2 == card_value_produkt_2
print("Название продукта №2 в корзине одинковое с названием продукта странеце OVERVIEW.")

"""Информация о цене продукта №1 в OVERVIEW."""
ovarview_prise_produkt_1 = driver_g.find_element(
    By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")    # Присваиваем переменной локатор цены продукта №1 в ovarview.
ovarview_prise_value_produkt_1 = ovarview_prise_produkt_1.text
print(
    f"Цена продукта №1 на странице OVERVIEW: {ovarview_prise_value_produkt_1}")

"""Информация о цене продукта №2 в OVERVIEW."""
ovarview_prise_produkt_2 = driver_g.find_element(
    By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")    # Присваиваем переменной локатор цены продукта №2 в ovarview.
ovarview_prise_value_produkt_2 = ovarview_prise_produkt_2.text
print(
    f"Цена продукта №2 на странице OVERVIEW: {ovarview_prise_value_produkt_2}")

"""Информация о итоговой цене покупки в Item total."""
sammary_prise_1 = driver_g.find_element(
    By.XPATH, "//div[@class = 'summary_subtotal_label']")   # Присваиваем значение переменной локатор суммы продукта №1 и №2 в Item total.
sammary_prise_1 = sammary_prise_1.text
print(f"Итоговая сумма - {sammary_prise_1}")

"""Удаяем знак '$" в спаРсеной строке продукта №1."""
str_1 = ovarview_prise_value_produkt_1  # Присваеваем переменой значение цены продукта №1.
int_1 = str_1[1:]   # Удаляем первый '$' элемент из строки.
print(f"Цена продукта № 1: {int_1}")    # Выводим цену продукта №1.

str_2 = ovarview_prise_value_produkt_2  # Присваеваем переменой значение цены продукта №2.
int_2 = str_2[1:]   # Удаляем первый '$' элемент из строки.
print(f"Цена продукта № 2: {int_2}")     # Выводим цену продукта №2.

summ_prise = float(int_1) + float(int_2)    # Переводим из строки в числа и складываем цену продукта №1 и №2.
print(f"Скалькулированная сумма двух товаров: {summ_prise}")   # Выводим сумму за продукт №1 и №2.

item_total = "Item total: $" + str(summ_prise)   # Присваиваем переменной значение полученной суммы.
print(f"Итоговая сумма {item_total}")
assert item_total == sammary_prise_1    # Сравниваем подщитанную сумму с цифрой в Item total
print(f"Сумма на странице OVERVIEW одинаковая с калькулированной суммой.")
