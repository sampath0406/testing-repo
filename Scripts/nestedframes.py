import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/nestedframes")
time.sleep(2)
driver.find_element(By.ID,"frame1")
driver.switch_to.parent_frame()
time.sleep(5)
driver.switch_to.frame(0)
txt = driver.find_element(By.XPATH,"//p[.='Child Iframe']").text
print(txt)
