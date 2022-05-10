import time

import allure
from selene.support.conditions.be import visible
from selene.support.shared import browser
from selene import by, be, have

from properties import MARKETPLACE
from src.pages.marketplace.complete_profile_page import CompleteProfile
from src.pages.marketplace.enter_magic_code_page import EnterMagicCodePage
from src.pages.marketplace.main_page import MainPage
from src.pages.marketplace.sign_in_page import SignInPage
from src.utils.randomizer import get_random_email

market_main_page = MainPage()
sign_in_page = SignInPage()
enter_magic_code_page = EnterMagicCodePage()
complete_profile_page = CompleteProfile()


# def test_user_sigh_up(open_prod_marketplace_page):
#     pass
