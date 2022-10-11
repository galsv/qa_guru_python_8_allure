from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("galsv/qa_guru_python_7_model").press_enter()

    s(by.link_text("galsv/qa_guru_python_7_model")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)