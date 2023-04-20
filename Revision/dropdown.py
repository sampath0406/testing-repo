from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/user/Desktop/dropdownweekdays.html")
# weekdays =Select(driver.find_element(By.ID, "weekdaysmenu"))
# weekdays.select_by_index(0)
# time.sleep(2)
# weekdays.select_by_visible_text('Tueday')
# time.sleep(2)
# weekdays.select_by_visible_text('Wednesday')
# time.sleep(2)
# weekdays.select_by_value('5')
# time.sleep(2)
# weekdays.select_by_index(5)
# time.sleep(2)
# weekdays.select_by_value('7')
# time.sleep(2)

cars = Select(driver.find_element(By.ID, "cars"))
time.sleep(5)
# list1 = cars.all_selected_options
# for i in list1:
#     print(i.text)

# first=cars.first_selected_option
# print(first.text)

op=cars.options
for i in op:
    print(i.text)