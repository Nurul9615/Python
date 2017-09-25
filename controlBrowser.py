#! python 3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
	elem = browser.find_element_by_class_name('bookcover')
	print('Found <%s> element with that class name!' % (elem.tag_name))
except:
	print('Was not able to find the element with that name')

linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-password')
passwordElem.send_keys('12345')
passwordElem.submit()

htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # Scroll to bottom
htmlElem.send_keys(Keys.HOME)