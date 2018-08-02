import unittest
from webdriver import Driver
from Values import strings
from Pages.key_presses import KeyPresses


class TestKeyPressing(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url + 'key_presses')

    def test_key_presses_alphabet(self):
        list_of_keys = {'G',
                        'A',
                        '9'}
        key_presses = KeyPresses(self.driver)
        if not key_presses.is_result_hidden():
            # report fail
            self.fail()
        for key in list_of_keys:
            key_presses.press_key(key)
            if key_presses.get_result() != "You entered: %s" % key:
                # report fail
                self.fail()
        else:
            # report pass
            print("PASS")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
