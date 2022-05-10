import allure
import pytest
from selene.support.shared import browser

from properties import MARKETPLACE


# helps to attach screenshots if test fails
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def open_prod_marketplace_page(request):
    browser.config.timeout = 10
    browser.open(MARKETPLACE['prod'])
    yield browser
    if request.node.rep_call.failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            allure.attach(browser.driver.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass

    browser.quit()
