# coding: utf8
from selenium import webdriver
import os 
import math


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_name("firstname")
firstname.send_keys("Test")

lastname = browser.find_element_by_name("lastname")
lastname.send_keys("Test")

email = browser.find_element_by_name("email")
email.send_keys("test@test.com")

file_input = browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           	# добавляем к этому пути имя файла 
file_input.send_keys(file_path)


send_button = browser.find_element_by_tag_name("button")
send_button.click()



