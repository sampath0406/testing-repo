import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/progress-bar")
time.sleep(2)
driver.find_element(By.ID,"startStopButton").click()
# time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(By.ID,"resetButton").click()
time.sleep(2)