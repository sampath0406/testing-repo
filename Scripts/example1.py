from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get("http://www.yahoo.com")
assert 'Yahoo' in browser.title
elem = browser.find_element(By.NAME,'p')
#Find the search box
elem.send_keys('seleniumq'+Keys.RETURN)
browser.quit()