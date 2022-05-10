from allure import step
from selene.support.shared import browser
from selene.support.conditions.be import visible

from src.pages.marketplace.sign_in_page import SignInPage


class MainPage:
    def __init__(self):
        self.sign_up_btn = browser.s('a.sign-up')
        self.log_in_btn = browser.s('a.log-in')
        self.cookie_acceptance_btn = browser.s('div a#hs-eu-confirmation-button')
        self.cookie_decline_btn = browser.s('div a#hs-eu-decline-button')
        self.explore_btn = browser.s('li#menu-item-341')
        self.create_btn = browser.s("a[title='Create']")
        self.help_center_btn = browser.s("a[title='Help Center']")

    @step('Click sign up button')
    def click_sign_up_btn(self):
        self.sign_up_btn.should_be(visible)
        self.sign_up_btn.click()

    @step('Click log in button')
    def click_log_in_btn(self):
        self.log_in_btn.click()

    @step('Click explore button')
    def click_explore_btn(self):
        self.explore_btn.click()

    @step('Click create button')
    def click_create_btn(self):
        self.create_btn.click()

    @step('Click help center button')
    def click_help_center_btn(self):
        self.help_center_btn.click()
