from allure import step
from selene.support.conditions.be import visible
from selene.support.shared import browser


class SignInPage:
    def __init__(self):
        self.email_or_number_field = browser.s('input[data-test-id]')
        self.send_magic_code_btn = browser.s('button#magiclink-btn')
        self.sign_in_with_metamask_btn = browser.s('i.fa-metamask')
        self.sign_in_with_slack_btn = browser.s('i.fa-slack')
        self.sign_in_with_facebook_btn = browser.s('i.fa-facebook-square')
        self.sign_in_with_google_btn = browser.s('i.fa-google')
        self.sign_in_with_linkedin_btn = browser.s('i.fa-linkedin')

    @step('Fill email field')
    def fill_email_field(self, value):
        self.email_or_number_field.should_be(visible)
        self.email_or_number_field.send_keys(value)

    @step('Click send magic code button')
    def click_send_magic_code_btn(self):
        self.send_magic_code_btn.should_be(visible)
        self.send_magic_code_btn.click()

    @step('Sign in with metamask button')
    def click_sign_in_with_metamask_btn(self):
        self.sign_in_with_metamask_btn.click()

    @step('Sign in with slack button')
    def click_sign_in_with_slack_btn(self):
        self.sign_in_with_slack_btn.click()

    @step('Sign in with facebook button')
    def click_sign_in_with_facebook_btn(self):
        self.sign_in_with_facebook_btn.click()

    @step('Sign in with google button')
    def click_sign_in_with_google_btn(self):
        self.sign_in_with_google_btn.click()

    @step('Sign in with linkedin button')
    def click_sign_in_with_linkedin_btn(self):
        self.sign_in_with_linkedin_btn.click()
