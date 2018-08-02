from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class KeyPresses:

    result = (By.ID, "result")
    content = (By.ID, "content")

    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        return self.driver.instance.find_element(*KeyPresses.result).text

    def press_key(self, key):
        actions = ActionChains(self.driver.instance)
        key = key.upper()
        actions.send_keys(key)
        actions.perform()

    def is_result_visible(self):
        if WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(KeyPresses.result)):
            return True
        else:
            return False

    def is_result_hidden(self):
        if WebDriverWait(self.driver.instance, 10).until(EC.invisibility_of_element_located(KeyPresses.result)):
            return True
        else:
            return False

