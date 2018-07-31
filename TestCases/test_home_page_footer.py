import unittest
from webdriver import Driver
from Values import strings
from Pages.home import Home


class TestHomePageFooter(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_page_footer(self):
        home = Home(self.driver)
        if not (home.is_footer_visible() or
                'Powered by Elemental Selenium' not in home.get_footer_text()):
            # report fail to reporting software
            self.fail()
        else:
            # report pass to reporting software
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
