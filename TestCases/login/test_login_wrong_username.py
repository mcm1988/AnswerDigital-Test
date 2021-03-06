import unittest
from webdriver import Driver
from Values import strings
from Pages.login import Login


class TestLoginWrongUsername(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url + "login")

    def test_login_wrong_username(self):
        login = Login(self.driver)
        username = 'incorrect'
        password = 'SuperSecretPassword!'
        login.set_username(username)
        login.set_password(password)
        login.click_submit()
        if (self.driver.instance.current_url != strings.base_url + "login" or
                'Your username is invalid!' not in login.get_flash_text()):
            # report fail to reporting software
            self.fail("FAIL")
        else:
            # report pass to reporting software
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
