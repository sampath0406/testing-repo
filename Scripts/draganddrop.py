import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/droppable")
time.sleep(2)
drag = driver.find_element(By.ID,"draggable")
time.sleep(1)
drop = driver.find_element(By.ID,"droppable")
actions = ActionChains(driver)
actions.drag_and_drop(drag, drop).perform()