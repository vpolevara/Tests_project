from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

class SauceDemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com"

    def open_page(self):
        self.driver.get(self.base_url)

    def login(self, username, password):
        user_name = self.driver.find_element(By.XPATH, "//input[@id = 'user-name']")
        user_name.send_keys(username)
        sleep(3)
        passw = self.driver.find_element(By.XPATH, "//input[@id = 'password']")
        passw.send_keys(password)
        sleep(2)
        but = self.driver.find_element(By.XPATH, "//input[@id = 'login-button']")
        but.click()
        sleep(3)

    def check_visibility(self, locator):
        try:
            element = EC.visibility_of_element_located(locator)
            return element
        except:
            return None

    def check_color_print(self, condition, message):
        if condition:
            print(f"{message} {Colors.GREEN}passed{Colors.END} !")
        else:
            print(f"{message} {Colors.RED}not passed{Colors.END} !")

    def test_false_data(self, false_username, password):
        self.login(false_username, password)
        check = self.check_visibility((By.XPATH, "//h3[@data-test='error']"))
        self.check_color_print(check, "False data test")

    def test_login(self, username, password):
        self.login(username, password)
        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Products']"))
        self.check_color_print(check, "Login test")

    def test_add_to_cart(self):
        buttons = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt"]
        for button_id in buttons:
            but = self.driver.find_element(By.XPATH, f"//button[@id = '{button_id}']")
            but.click()
            sleep(3)

        check = self.check_visibility((By.XPATH, "//button[@id = 'remove-sauce-labs-backpack']"))
        self.check_color_print(check, "Add test")

    def test_shopping_cart(self):
        but = self.driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']")
        but.click()
        sleep(2)
        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Your Cart']"))
        self.check_color_print(check, "Shopping cart test")

    def test_continue_shopping(self):
        but = self.driver.find_element(By.XPATH, "//button[@id = 'continue-shopping']")
        but.click()
        sleep(2)
        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Products']"))
        self.check_color_print(check, "Continue shopping test")

    def test_remove_from_cart(self):
        but = self.driver.find_element(By.XPATH, "//button[@id = 'remove-sauce-labs-backpack']")
        but.click()
        sleep(4)
        check = self.check_visibility((By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']"))
        self.check_color_print(check, "Remove test")

    def test_checkout_button(self):
        but = self.driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']")
        but.click()
        sleep(2)
        but = self.driver.find_element(By.XPATH, "//button[@id = 'checkout']")
        but.click()
        sleep(2)
        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']"))
        self.check_color_print(check, "Checkout button test")

    def test_input_last_name(self, name, surname, code):
        first_name = self.driver.find_element(By.XPATH, "//input[@id = 'first-name']")
        first_name.send_keys(name)
        sleep(2)
        last_name = self.driver.find_element(By.NAME, "lastName")
        last_name.send_keys(surname)
        sleep(2)
        postal_code = self.driver.find_element(By.XPATH, "//input[@id = 'postal-code']")
        postal_code.send_keys(code)
        sleep(2)
        but = self.driver.find_element(By.XPATH, "//input[@id = 'continue']")
        but.click()
        sleep(2)
        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Checkout: Overview']"))
        self.check_color_print(check, "Input last name test")

    def test_finish_button(self):
        but = driver.find_element(By.XPATH, "//button[@id = 'finish']")
        but.click()
        sleep(2)

        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']"))
        self.check_color_print(check, "Finish button test")
        sleep(3)

    def test_back_home_button(self):
        but = driver.find_element(By.XPATH, "//button[@id = 'back-to-products']")
        but.click()
        sleep(2)

        check = self.check_visibility((By.XPATH, "//span[@class='title' and text()='Products']"))
        self.check_color_print(check, "Back home button test")
        sleep(3)



    def test_logout(self):
        but = self.driver.find_element(By.XPATH, "//button[@id = 'react-burger-menu-btn']")
        but.click()
        sleep(2)
        but = self.driver.find_element(By.XPATH, "//a[@id = 'logout_sidebar_link']")
        but.click()
        sleep(2)
        check = self.check_visibility((By.XPATH, "//div[@class='login_credentials_wrap-inner']"))
        self.check_color_print(check, "Logout test")
        sleep(3)
    
    

driver = webdriver.Safari() # do zmiany
driver.maximize_window()
test_page = SauceDemoPage(driver)

test_page.open_page()
test_page.test_false_data('user', 'secret_sauce')
driver.refresh()
test_page.test_login('standard_user', 'secret_sauce')
test_page.test_add_to_cart()
test_page.test_shopping_cart()
test_page.test_continue_shopping()
test_page.test_remove_from_cart()
test_page.test_checkout_button()
test_page.test_input_last_name('Nika', 'Pol', '123-456')
test_page.test_finish_button()
test_page.test_back_home_button()
test_page.test_logout()

driver.quit()
