import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/upload-download")
time.sleep(2)
file_path = r"C:\Users\R.K GOWDA\Downloads\add.pdf"
find_input = driver.find_element(By.ID,"uploadFile").send_keys(file_path)
time.sleep(2)
