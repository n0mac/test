import unittest
from selenium import webdriver
import HTMLTestRunner
import page


class TESTLOGIN(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://admin.mountaintrek.com/"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_invalid_login_user(self):

        #PRECONDITIONS
        self.driver.get(self.base_url)
        login_page = page.LoginPage(self.driver)
        asserts = page.AssertIDs(self.driver)

        #CHECK THAT USER IS ON LOGIN PAGE
        login_page.is_opened()

        #ENTER VALID EMAIL AND INVALID PASSWORD
        login_page.input_email_sign_in("test@mev.com")
        login_page.input_password_field("qweqwe123")
        login_page.click_login_button()
        login_page.wait_until_ok_is_present()

        #CHECK THAT VALIDATION ERROR IS DISPLAYED
        login_page.invalid_email_or_password_popup_is_displayed()

        #CLOSE VALIDATION POP-UP
        login_page.click_ok_button()

    def test_valid_login_user(self):

        #PRECONDITIONS
        self.driver.get(self.base_url)
        login_page = page.LoginPage(self.driver)
        practical_guide_page = page.PracticalGuidePage(self.driver)
        asserts = page.AssertIDs(self.driver)

        #CHECK THAT USER IS ON LOGIN PAGE
        login_page.is_opened()

        #ENTER VALID EMAIL AND PASSWORD
        login_page.input_email_sign_in("test@mev.com")
        login_page.input_password_field("12345678")
        login_page.click_login_button()

        #WAIT UNTIL USER IS LOGGED IN TO ADMIN PANEL, REDIRECTED TO PRACTICAL GUIDE PAGE
        login_page.wait_until_practical_guide_page_opened()

        #CHECK THAT USER IS LOGGED IN ADN REDIRECTED TO PRACTICAL GUIDE PAGE
        practical_guide_page.is_opened()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    HTMLTestRunner.main()

