from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
buttons = driver.find_element(By.ID,"doubleClickBtn")
actions = ActionChains(driver)
actions.double_click(buttons).perform()
txt = driver.find_element(By.ID,"doubleClickMessage").text
print(txt)