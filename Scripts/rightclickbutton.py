import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
time.sleep(2)
btn = driver.find_element(By.ID,"rightClickBtn")
action = ActionChains(driver)
action.context_click(btn).perform()
msg = driver.find_element(By.ID,"rightClickMessage").text
print(msg)