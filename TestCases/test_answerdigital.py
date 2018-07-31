import unittest
from webdriver import Driver
from Values import strings
from Pages.home import Home


class TestAnswerDigitalTest(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = Home(self.driver)
        home_screen.validate_content_is_present()
        home_screen.validate_footer_is_present()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
