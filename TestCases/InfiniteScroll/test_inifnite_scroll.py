import unittest
from webdriver import Driver
from Values import strings
from Pages.inifnite_scroll import InfiniteScroll


class TestInfiniteScroll(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url + 'infinite_scroll')

    def test_infinite_scroll(self):
        infinite_scroll = InfiniteScroll(self.driver)
        if not infinite_scroll.page_ready():
            # report fail
            self.fail()
        amount_of_texts = infinite_scroll.get_number_of_texts()
        scrolls_done = 0

        while scrolls_done < 2:
            infinite_scroll.scroll_down()
            infinite_scroll.load_complete()
            new_amount_of_texts = infinite_scroll.get_number_of_texts()
            if not new_amount_of_texts > amount_of_texts:
                # report fail
                self.fail()
            else:
                amount_of_texts = new_amount_of_texts
            scrolls_done += 1
        infinite_scroll.scroll_to_top()
        new_amount_of_texts = infinite_scroll.get_number_of_texts()
        if not new_amount_of_texts == amount_of_texts:
            # report fail
            self.fail()
        else:
            # report pass
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
