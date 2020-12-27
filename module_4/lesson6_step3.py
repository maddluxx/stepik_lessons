import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    #time.sleep(10)
    browser.quit()

@pytest.mark.parametrize('lesson', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_answer_correct(browser, lesson):
    link = f"https://stepik.org/lesson/236{lesson}/step/1"
    browser.get(link)
    input_answer = browser.find_element_by_css_selector(".quiz-component.ember-view textarea")
    button = browser.find_element_by_css_selector(".submit-submission")
    answer = str(math.log(int(time.time())))
    input_answer.send_keys(answer)
    button.click()
    hint_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert hint_text == 'Correct!', f"Aliens have been spotted! Their message:{hint_text}"
