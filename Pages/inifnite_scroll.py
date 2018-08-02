from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions


class InfiniteScroll:

    jscroll_container = (By.CLASS_NAME, "jscroll-inner")
    jscrolls = (By.CLASS_NAME, "jscroll-added")
    jscroll_loading = (By.CLASS_NAME, "jscroll-loading")
    content = (By.ID, "content")

    def __init__(self, driver):
        self.driver = driver

    def get_number_of_texts(self):
        return len(self.driver.instance.find_elements(*InfiniteScroll.jscrolls))

    def scroll_down(self):
        self.driver.instance.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        actions = ActionChains(self.driver.instance)
        actions.send_keys(Keys.CONTROL + Keys.HOME)
        actions.perform()

    def page_ready(self):
        try:
            WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(InfiniteScroll.content))
        except exceptions.TimeoutException:
            return False
        else:
            return True

    def load_complete(self):
        try:
            WebDriverWait(self.driver.instance, 5).until_not(EC.presence_of_element_located(InfiniteScroll.jscroll_loading))
        except exceptions.TimeoutException:
            return False
        else:
            return True

