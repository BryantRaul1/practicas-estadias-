from allure import step
from selene.support.shared import browser


class CompleteProfile:
    def __init__(self):
        self.full_name_field = browser.s("input[placeholder='Full Name']")
        self.mobile_number_field = browser.s("input[placeholder='Mobile number']")
        self.update_profile_btn = browser.s('button[data-test-id]')

    @step('Fill full name field')
    def fill_full_name_field(self, value):
        self.full_name_field.send_keys(value)

    @step('Fill mobile number field')
    def fill_mobile_number_field(self, value):
        self.mobile_number_field.send_keys(value)

    @step('Click update profile button')
    def click_update_profile_btn(self):
        self.update_profile_btn.click()
