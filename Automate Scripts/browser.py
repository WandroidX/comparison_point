from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://www.youtube.com')
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
browser.find_element_by_id('text').send_keys(Keys.CONTROL + 't')
