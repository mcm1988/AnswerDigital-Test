import unittest
from webdriver import Driver
from Values import strings
from Pages.home import Home


class TestHomePageContent(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_page_content(self):
        home = Home(self.driver)
        if not home.is_content_visible():
            # report fail
            self.fail()
        else:
            # report pass
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
