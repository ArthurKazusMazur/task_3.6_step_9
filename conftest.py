import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en",
                     help='Please, choose your browser_language: en, es, ru, fr, etc...')


@pytest.fixture()
def browser(request):
    print("\n\n"+"Start browser for test")
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\n\n"+"Quit browser")
    browser.quit()
