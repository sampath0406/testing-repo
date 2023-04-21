import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
time.sleep(2)
driver.find_element(By.ID,"WftB3").click()
txt = driver.find_element(By.ID,"dynamicClickMessage").text
time.sleep(2)
print(txt)