import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/select-menu")
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='Select Title']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='Mr.']").click()
time.sleep(2)
drpdown = driver.find_element(By.ID,"oldSelectMenu")
select = Select(drpdown)
select.select_by_index(2)
time.sleep(2)
