import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web", 'test')
@allure.severity(Severity.MINOR)
@allure.label("Sergey")
@allure.description("This is descrition")
@allure.feature("Allure with step")
@allure.story("Check issue")
@allure.link("https://github.com")
def test_github_with_allure_steps():
    with allure.step("Open main site"):
        browser.open("https://github.com")

    with allure.step("Input repo name and find repo"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("galsv/qa_guru_python_7_model").press_enter()

    with allure.step("Click on findy repo"):
        s(by.link_text("galsv/qa_guru_python_7_model")).click()

    with allure.step("Click on issue's link"):
        s("#issues-tab").click()

    with allure.step("Check visible link or not"):
        s(by.partial_text("#1")).should(be.visible)
