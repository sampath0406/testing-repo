import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
time.sleep(2)
driver.find_element(By.ID,"tabButton").click()
time.sleep(2)
