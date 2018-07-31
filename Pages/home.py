from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home:

    content = By.ID, 'content'
    footer = By.ID, 'page-footer'

    def __init__(self, driver):
        self.driver = driver

    def get_content_text(self):
        return self.driver.instance.find_element(*Home.content).text

    def get_footer_text(self):
        return self.driver.instance.find_element(*Home.footer).text

    def is_content_visible(self):
        try:
            WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(Home.content))
        except exceptions.TimeoutException:
            return False
        else:
            return True

    def is_footer_visible(self):
        try:
            WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(Home.footer))
        except exceptions.TimeoutException:
            return False
        else:
            return True
