# coding: utf8
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

name_input = browser.find_element_by_css_selector(".first_block .first_class input")
name_input.send_keys("Ivan")
surname_input = browser.find_element_by_css_selector(".first_block .second_class input")
surname_input.send_keys("Ivanov")
email_input = browser.find_element_by_css_selector(".first_block .third_class input")
email_input.send_keys("test@mail.com")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text