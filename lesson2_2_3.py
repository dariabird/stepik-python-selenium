# coding: utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

a = int(browser.find_element_by_id("num1").text)
b = int(browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(a + b))

send_button = browser.find_element_by_tag_name("button")
send_button.click()

