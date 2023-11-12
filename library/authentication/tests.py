import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
def login_selenium(username, password):
    n = 0
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")
    login_btn = driver.find_element(By.XPATH, '//a[@href="login" and @class="btn btn-outline-primary btn-lg btn-block"]')
    time.sleep(n)
    login_btn.click()
    time.sleep(n)
    login_username = driver.find_element(By.XPATH, '//input[@id="id_username"]')
    login_username.send_keys(username)
    login_password = driver.find_element(By.XPATH, '//input[@id="id_password"]')
    login_password.send_keys(password)
    login_enter_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    time.sleep(n)
    login_enter_btn.click()
    time.sleep(n)
    try:
        logout_btn = driver.find_element(By.XPATH, '//a[@href="/logout/"]')
        log_test = logout_btn.text
        time.sleep(n)
    except:
        log_message = driver.find_element(By.XPATH, '//div[@class="alert alert-primary"]')
        log_test = log_message.text
    return log_test


def logout_selenium():
    n = 0
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    login_btn = driver.find_element(By.XPATH, '//a[@href="login" and @class="btn btn-outline-primary btn-lg btn-block"]')
    time.sleep(n)
    login_btn.click()
    time.sleep(n)
    login_username = driver.find_element(By.XPATH, '//input[@id="id_username"]')
    login_username.send_keys("vova@ukr.net")
    login_password = driver.find_element(By.XPATH, '//input[@id="id_password"]')
    login_password.send_keys('admin')
    login_enter_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    time.sleep(n)
    login_enter_btn.click()
    time.sleep(n)
    logout_btn = driver.find_element(By.XPATH, '//a[@href="/logout/"]')
    time.sleep(n)
    logout_btn.click()
    time.sleep(n)
    try:
        login_btn = driver.find_element(By.XPATH, '//a[@href="login" and @class="btn btn-outline-primary btn-lg btn-block"]')
        return login_btn.text
    except:
        return "Помилка: Користувач не мав можливості вийти із системи"


class AuthenticationTestCase(TestCase):

    def test_1_login_correct(self):
        correct_username = "vova@ukr.net"
        correct_password = "admin"
        expected = "Вихід"
        actual = login_selenium(correct_username, correct_password)
        self.assertEqual(actual, expected)

    def test_2_login_wrong(self):
        wrong_username = "vov@ukr.net"
        wrong_password = "admin"
        expected = "Помилка: Логін або пароль не вірні!"
        actual = login_selenium(wrong_username, wrong_password)
        self.assertEqual(actual, expected)

    def test_logout(self):
        exected = "Вхід"
        actual = logout_selenium()
        self.assertEqual(actual, exected)

