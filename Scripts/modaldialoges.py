import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/modal-dialogs")
time.sleep(2)
driver.find_element(By.ID,"showSmallModal").click()
time.sleep(2)
txt =driver.find_element(By.XPATH,"//div[@class='modal-body']").text
print(txt)
driver.find_element(By.ID,"closeSmallModal").click()
time.sleep(5)