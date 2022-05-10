import time

from allure import title
from selene.support.conditions.be import visible, clickable

from src.data.user import valid_user_email
from src.pages.marketplace.complete_profile_page import CompleteProfile
from src.pages.marketplace.enter_magic_code_page import EnterMagicCodePage
from src.pages.marketplace.main_page import MainPage
from src.pages.marketplace.sign_in_page import SignInPage
from src.utils.mailosaur_helper import Mailosaur
from src.utils.randomizer import get_random_email

market_main_page = MainPage()
sign_in_page = SignInPage()
enter_magic_code_page = EnterMagicCodePage()
complete_profile_page = CompleteProfile()


@title('User login test')
def test_login(open_prod_marketplace_page):
    market_main_page.click_log_in_btn()
    sign_in_page.fill_email_field(valid_user_email)
    sign_in_page.click_send_magic_code_btn()
    mailosaur = Mailosaur(valid_user_email)
    code = mailosaur.get_return_code()
    enter_magic_code_page.fill_magic_code_field(code)
    enter_magic_code_page.click_verify_btn()
    time.sleep(0.5)
    complete_profile_page.click_update_profile_btn()
    market_main_page.explore_btn.should_be(visible)
    mailosaur.delete_letter()

@title('Test user sigh up')
def test_user_sigh_up(open_prod_marketplace_page):
    user_email = get_random_email()
    market_main_page.click_sign_up_btn()
    sign_in_page.fill_email_field(user_email)
    sign_in_page.click_send_magic_code_btn()
    mailosaur = Mailosaur(user_email)
    code = mailosaur.get_return_code()
    enter_magic_code_page.fill_magic_code_field(code)
    enter_magic_code_page.click_verify_btn()
    time.sleep(0.5)

    complete_profile_page.fill_full_name_field('Test User')
    complete_profile_page.click_update_profile_btn()
    market_main_page.explore_btn.should_be(visible)
    mailosaur.delete_letter()
