from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)

    # таким элегантным образом я реализовал "assert"
    add_to_basket_button = WebDriverWait(browser, 5). \
        until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')),
              "К сожалению, кнопка не найдена")

    # нет необходимости добавлять time.sleep(30), т.к. название кнопки будет выведено на печать в консоли
    # после запуска теста командой "pytest -s --language=fr test_items.py"
    print("\n\n"+add_to_basket_button.text)
