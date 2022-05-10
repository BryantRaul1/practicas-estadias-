from allure import step
from selene.support.shared import browser
from src.utils.mailosaur_helper import Mailosaur


class EnterMagicCodePage:
    def __init__(self):
        self.input_magic_code_field = browser.s('input[data-test-id]')
        self.verify_btn = browser.s('button.button')

    @step('Fill magic code field from mailosaur')
    def fill_magic_code_field(self, code):
        self.input_magic_code_field.send_keys(code)

    @step('Click verify button')
    def click_verify_btn(self):
        self.verify_btn.click()
