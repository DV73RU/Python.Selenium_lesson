# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://academyopen.ru/'
driver_g.get(base_url)
driver_g.maximize_window()
registration = driver_g.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[2]/div/button/span')
registration.click()

login = driver_g.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[2]/div/div/div[2]/a')
login.click()
tel_number = driver_g.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/div/div[2]/div[1]/form/div/div[3]/div/input')
tel_number.send_keys('1234567890')

# Функция нажатия на чек бокс
# Функция нажатия на кнопку "Получить код"
# Функция воода кода.
# ... ...
# button_login = driver_g.find_element(By.ID, 'login-button')
# button_login.click()

# time.sleep(10)
# driver_g.close()


#  //*[@id="__next"]/div[1]/header/div[1]/div[2]/div/button/span