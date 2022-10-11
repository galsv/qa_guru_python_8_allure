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
def test_github_with_allure_decorate_steps():
    open_main_page()
    searching_repo()
    click_lynk()
    go_to_issues()
    check_issue()


@allure.step("Open main site")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Input repo name and find repo")
def searching_repo():
    s(".header-search-input").click()
    s(".header-search-input").send_keys("galsv/qa_guru_python_7_model").press_enter()

@allure.step("Click on findy repo")
def click_lynk():
    s(by.link_text("galsv/qa_guru_python_7_model")).click()


@allure.step("Click on issue's link")
def go_to_issues():
    s("#issues-tab").click()


@allure.step("Check visible link or not")
def check_issue():
    s(by.partial_text("#1")).should(be.visible)
