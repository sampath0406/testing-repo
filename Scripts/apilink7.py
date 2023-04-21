import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/links")
time.sleep(2)
driver.find_element(By.ID,"invalid-url").click()
time.sleep(2)
txt = driver.find_element(By.ID,"linkResponse").text
print(txt)