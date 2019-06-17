# coding: utf8
from selenium import webdriver

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_id("button")