# coding: utf8
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(3)

want_button = browser.find_element_by_tag_name("button")
want_button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

text_input = browser.find_element_by_name("text")
text_input.send_keys(y)

send_button = browser.find_element_by_tag_name("button")
send_button.click()



