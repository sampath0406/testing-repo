import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")
driver.find_element(By.CLASS_NAME, "rct-checkbox").click()
time.sleep(2)
txt = driver.find_element(By.ID,"result").text
print(txt)
