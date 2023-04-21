import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/upload-download")
time.sleep(2)
driver.find_element(By.ID,"downloadButton").click()
time.sleep(2)