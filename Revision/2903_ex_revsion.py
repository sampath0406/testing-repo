import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/user/Desktop/ex.html")
driver.find_element(By.NAME, "username").send_keys('admin')
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('admin')
login_form1 = driver.find_element(By.XPATH,"//input[@id='loginForm']")
print(login_form1.('outerHTML'))

time.sleep(5)