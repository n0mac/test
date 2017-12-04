from selenium.webdriver.common.by import By

class SignInLocators(object):
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "passwordPlain")
    LOGIN_BUTTON = (By.XPATH, ".//*[@id='button-1017-btnEl']")
    OK_BUTTON = (By.LINK_TEXT, "OK")
    OK_BUTTON_NEGATIVE = (By.XPATH, "Oh_no")
    FORGOT_PASSWORD_BUTTON = (By.LINK_TEXT, "Forgot Password?")

class AssertTitles(object):
    SIGN_IN_TITLE = "Sign In"
    INVALID_EMAIL_PASSWORD = "Invalid email or password"
    ADMIN_NOT_ACTIVE = "Admin is not active"
    PRACTICAL_GUIDE_OPENED = "Practical Guide"

class GmailLocators(object):
    GMAIL_EMAIL = (By.NAME, "Email")
    GMAIL_PWD = (By.NAME, "Passwd")
    NEXT_BUTTON = (By.ID, "next")
    SIGN_IN_BUTTON = (By.ID, "signIn")
    MAIL_ID = (By.XPATH, "//div [@class='y6']/span[contains(.,'Mountain Trek Password Recovery')]")
    RESET_PWD_MAIL = (By.LINK_TEXT, "Reset password")


class ForgotPasswordLocators(object):
    SEND_EMAIL_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/div/input")
    INPUT_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input")
    GO_TO_ADMIN_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/a")
    NEW_PWD_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input[1]")
    CONFIRM_PWD_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input[2]")
    RESET_PWD_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/div/input")
