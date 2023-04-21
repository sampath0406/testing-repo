import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
time.sleep(2)
driver.find_element(By.ID,"alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID,"timerAlertButton").click()
time.sleep(6)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)