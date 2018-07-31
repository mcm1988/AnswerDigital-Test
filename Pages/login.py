from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    login_form = By.ID, 'login'
    username = By.ID, 'username'
    password = By.ID, 'password'
    flash = By.ID, 'flash'
    submit = By.XPATH, '//*[@id="login"]/button'
    logout_button = By.XPATH, '//*[@id="content"]/div/a'

    def __init__(self, driver):
        self.driver = driver

    def get_flash_text(self):
        return self.driver.instance.find_element(*Login.flash).text

    def get_username(self):
        return self.driver.instance.find_element(*Login.username)

    def get_password(self):
        return self.driver.instance.find_element(*Login.password)

    def set_username(self, username):
        self.get_username().send_keys(username)

    def set_password(self, password):
        self.get_password().send_keys(password)

    def click_submit(self):
        self.driver.instance.find_element(*Login.submit).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_submit()

    def click_logout(self):
        self.driver.instance.find_element(*Login.logout_button).click()

    def is_login_form_visible(self):
        try:
            WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(Login.login_form))
        except exceptions.TimeoutException:
            return False
        else:
            return True

