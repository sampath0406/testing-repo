import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/radio-button")
time.sleep(5)
driver.find_element(By.XPATH,"//label[text()='Yes']").click()
time.sleep(5)
txt = driver.find_element(By.XPATH,"//span[text()='Yes']").text
print(txt)