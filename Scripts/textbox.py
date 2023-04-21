import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(2)
driver.find_element(By.ID,"userName").send_keys("Rakesh")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("rakesh@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"currentAddress").send_keys("Hassan")
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys("Hirisave")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.ID,"submit").click()
time.sleep(3)
