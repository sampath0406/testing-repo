import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/frames")
time.sleep(2)
driver.find_element(By.ID,"frame1")
driver.switch_to.frame("frame1")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500);")
txt = driver.find_element(By.ID,"sampleHeading").text
print(txt)
driver.switch_to.default_content()
time.sleep(5)
driver.find_element(By.ID,"frame2")
driver.switch_to.frame("frame2")
txt1 = driver.find_element(By.ID,"sampleHeading").text
print(txt1)
time.sleep(2)