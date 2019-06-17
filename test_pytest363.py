import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])
def test_get_correct_message(browser, link):
    browser.get(link)
    answer_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
    )
    answer = math.log(int(time.time()))
    print(answer)
    answer_input.send_keys(str(answer))
    send_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".submit-submission"))
        )
    send_button.click()
    ok_label = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".attempt__message"))
        )
    correct_label = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    #correct_label = browser.find_element_by_css_selector(".smart-hints__hint")
    assert correct_label.text == "Correct!"
