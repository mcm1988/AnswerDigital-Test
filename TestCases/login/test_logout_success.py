import unittest
from webdriver import Driver
from Values import strings
from Pages.login import Login


class TestLogoutSuccess(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url + "login")

    def test_logout_success(self):
        login = Login(self.driver)
        username = 'tomsmith'
        password = 'SuperSecretPassword!'
        login.login(username, password)
        login.click_logout()
        if (self.driver.instance.current_url != strings.base_url + "login" or
                'You logged out of the secure area!' not in login.get_flash_text()):
            # report fail to reporting software
            self.fail("FAIL")
        else:
            # report pass to reporting software
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
