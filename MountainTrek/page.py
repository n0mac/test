from selenium.common.exceptions import NoSuchElementException
from locators import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.exeption = NoSuchElementException


class LoginPage(BasePage):

    def invalid_email_or_password_popup_is_displayed(self):
        assert AssertTitles.INVALID_EMAIL_PASSWORD in self.driver.page_source

    def is_opened(self):
        assert AssertTitles.SIGN_IN_TITLE in self.driver.page_source

    def input_email_sign_in(self, email):
        email_field = self.driver.find_element(*SignInLocators.EMAIL_FIELD)
        email_field.send_keys(email)


    def input_password_field(self, password):
        input_pass = self.driver.find_element(*SignInLocators.PASSWORD_FIELD)
        input_pass.send_keys(password)

    def click_login_button(self):
        click_login = self.driver.find_element(*SignInLocators.LOGIN_BUTTON)
        click_login.click()

    def wait_until_ok_is_present(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(((By.XPATH, ".//*[@id='button-1005']")))
            )
        finally:
            pass

    def click_ok_button(self):
        ok_button = self.driver.find_element(*SignInLocators.OK_BUTTON)
        ok_button.click()

    def clear_email_sign_in(self):
        email_field_clear = self.driver.find_element(*SignInLocators.EMAIL_FIELD)
        email_field_clear.clear()

    def clear_password_field(self):
        clear_pass = self.driver.find_element(*SignInLocators.PASSWORD_FIELD)
        clear_pass.clear()

    def wait_until_practical_guide_page_opened(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "x-grid-item")))
        finally:
            pass

class PracticalGuidePage(BasePage):
    def is_opened(self):
        assert AssertTitles.PRACTICAL_GUIDE_OPENED in self.driver.page_source

class ForgotPasswordFunctionality(BasePage):
    def click_forgot_password(self):
        click_forgot = self.driver.find_element(*SignInLocators.FORGOT_PASSWORD_BUTTON)
        click_forgot.click()

    def open_gmail_in_new_tab(self):
        elem = self.driver.find_element(*SignInLocators.FORGOT_PASSWORD_BUTTON)
        elem.send_keys(Keys.COMMAND + 't')
        self.driver.get("https://mail.google.com")

    def enter_email_gmail(self, param1):
        email_login = self.driver.find_element(*GmailLocators.GMAIL_EMAIL)
        email_login.send_keys(param1)

    def enter_email_pwd(self, param1):
        email_pwd = self.driver.find_element(*GmailLocators.GMAIL_PWD)
        email_pwd.send_keys(param1)

    def click_next(self):
        next_button = self.driver.find_element(*GmailLocators.NEXT_BUTTON)
        next_button.click()

    def click_sign_in(self):
        sign_in = self.driver.find_element(*GmailLocators.SIGN_IN_BUTTON)
        sign_in.click()

    def click_correct_mail(self):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((GmailLocators.MAIL_ID))
            )
            element.click()
        finally:
            pass
            #click_mail = self.driver.find_element(*GmailLocators.MAIL_ID)
            #click_mail.click()

    def input_forgot_email(self, param1):
        input_forgot_email = self.driver.find_element(*ForgotPasswordLocators.INPUT_FIELD)
        input_forgot_email.send_keys(param1)

    def click_send_email(self):
        send_button = self.driver.find_element(*ForgotPasswordLocators.SEND_EMAIL_BUTTON)
        send_button.click()

    def click_go_to_admin(self):
        click_go_admin = self.driver.find_element(*ForgotPasswordLocators.GO_TO_ADMIN_BUTTON)
        click_go_admin.click()

    def click_reset_password_mail(self):
        click_reset = self.driver.find_element(*GmailLocators.RESET_PWD_MAIL)
        click_reset.click()

    def input_new_pwd(self, param1):
        input_new_pwd = self.driver.find_element(*ForgotPasswordLocators.NEW_PWD_FIELD)
        input_new_pwd.send_keys(param1)

    def input_confitm_pwd(self, param1):
        input_confirm = self.driver.find_element(*ForgotPasswordLocators.CONFIRM_PWD_FIELD)
        input_confirm.send_keys(param1)

    def clear_new_pwd(self):
        clear_field = self.driver.find_element(*ForgotPasswordLocators.NEW_PWD_FIELD)
        clear_field.clear()

    def clear_confirm_pwd(self):
        clear_field = self.driver.find_element(*ForgotPasswordLocators.CONFIRM_PWD_FIELD)
        clear_field.clear()

    def click_reset_your_password(self):
        click_reset_pwd = self.driver.find_element(*ForgotPasswordLocators.RESET_PWD_BUTTON)
        click_reset_pwd.click()

class AssertIDs(BasePage):
    def login_page_title(self):
        return AssertTitles.SIGN_IN_TITLE

    def validation_error(self):
        return AssertTitles.INVALID_EMAIL_PASSWORD

    def not_active_admin_error(self):
        return AssertTitles.ADMIN_NOT_ACTIVE

    def practical_guide_page_opened(self):
        return AssertTitles.PRACTICAL_GUIDE_OPENED