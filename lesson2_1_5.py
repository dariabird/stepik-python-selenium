# coding: utf8
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

robot_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
robot_checkbox.click()

robot_radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
robot_radiobutton.click()

send_button = browser.find_element_by_tag_name("button")
send_button.click()

