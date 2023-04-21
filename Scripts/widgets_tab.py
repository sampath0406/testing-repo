import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/tabs")
time.sleep(2)
driver.find_element(By.ID,"demo-tab-origin").click()
time.sleep(2)
txt = driver.find_element(By.ID,"demo-tabpane-origin").text
print(txt)
driver.find_element(By.ID,"demo-tab-use").click()
time.sleep(2)
txt1 = driver.find_element(By.ID,"demo-tabpane-use").text
print(txt1)
driver.find_element(By.ID,"demo-tab-what").click()
time.sleep(2)
txt2 = driver.find_element(By.ID,"demo-tabpane-what").text
print(txt2)