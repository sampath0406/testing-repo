import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")
driver.find_element(By.ID,"addNewRecordButton").click()
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys("rakesh")
time.sleep(2)
driver.find_element(By.ID,"lastName").send_keys("gowda")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("rakesh@123.gmail.com")
time.sleep(2)
driver.find_element(By.ID,"age").send_keys(27)
time.sleep(2)
driver.find_element(By.ID,"salary").send_keys(25000)
time.sleep(2)
driver.find_element(By.ID,"department").send_keys("Testing")
time.sleep(2)
driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.find_element(By.ID,"delete-record-4").click()
time.sleep(3)