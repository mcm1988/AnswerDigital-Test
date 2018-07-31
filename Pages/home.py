from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Values import strings


class Home:

    def __init__(self, driver):
        self.driver = driver
        self.content = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "content")))
        self.footer = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "page-footer")))

    def validate_content_is_present(self):
        assert self.content.is_displayed()

    def validate_footer_is_present(self):
        assert self.footer.is_displayed()
