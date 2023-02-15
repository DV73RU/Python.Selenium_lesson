from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

# Создаем cookie
private static final Cookie COOKIE = new Cookie("имя", "содержимое", "домен", "путь", new Date("дата"));
# Создаем браузер
WebDriver driver = new ChromeDriver(options);
# Добавляем cookie в браузер
driver.manage().addCookie(COOKIE);

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
g = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://academyopen.ru/'
driver_g.get(base_url)
driver_g.maximize_window()

number = 1234567890     # Номер телефона
code = 9876     # cmc код

registration = driver_g.find_element(
    By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[2]/div/button/span')
registration.click()
print(Fore.BLUE + "Нажата кнопка регистрация и вход")
login = driver_g.find_element(
    By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[2]/div/div/div[2]/a')
login.click()
print(Fore.BLUE + "Нажата кнопка 'войти' в pop-up окне")
# Ищем заголовок страници автиоризации.
pages_login = driver_g.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/div/div[2]/div[1]/form/div/div[1]')
value_pages_login = pages_login.text
assert value_pages_login == 'Вход для участников Академии бизнеса'
print(Fore.BLUE + 'Страница авторизации - найдена')
tel_number = driver_g.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/div/div[2]/div[1]/form/div/div[3]/div/input')
tel_number.send_keys(number)
print(Fore.BLUE + "Введен номер телефона")
# Находим чекбокс
checkbox = driver_g.find_element(
    By.XPATH, "//span[@class='checkbox__icon']")   # Ищем локатор чек бокс
# Кликаем на чек бокс
checkbox.click()

# Ищем локатор кнопки "Получить код"
button = driver_g.find_element(
    By.XPATH, "//button[@class = 'button button--register']")
button.click()
time.sleep(2)
# Проверяем что открыто окно для ввода смс кода
# Ищем на странице текст "Подтвердите номер телефона".
pages_sms_code = driver_g.find_element(
    By.XPATH, "//div[@class='register__title']")
value_pages_sms_code = pages_sms_code.text
assert value_pages_sms_code == 'Подтвердите номер телефона'
print(Fore.BLUE + 'Страница подтверждения смс кода - найдена')

# Вводим в поле код смс
time.sleep(2)
# Ищем поле ввода кода смс.
code_sms = driver_g.find_element(
    By.XPATH, "//*[@id='__next']/div/main/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/form/div/div/input[1]")
code_sms.send_keys(code)
time.sleep(2)
# Проверяем открыто окно автогризованной странице.
# Ищем на странице текст "ЛИЧНЫЙ КАБИНЕТ".
pages_authorized = driver_g.find_element(
    By.XPATH, "//h1[@class='page_lk__title']")
value_pages_authorized = pages_authorized.text
assert value_pages_authorized == 'ЛИЧНЫЙ КАБИНЕТ'
print(Fore.BLUE + 'Авторизоввнная страница - найдена')


# // TODO Функция нажатия на кнопку "Получить код"
# // TODO Функция воода кода.
