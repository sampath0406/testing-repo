import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
time.sleep(2)
driver.find_element(By.ID,"windowButton").click()
time.sleep(2)
handle = driver.window_handles
driver.switch_to.window(handle[-1])
time.sleep(2)