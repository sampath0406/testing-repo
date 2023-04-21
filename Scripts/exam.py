# list = [1, 2,3,4,5]
# rev_list= list[::-1]
# print(rev_list)
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# def test_search_watch(browser):
#     browser.get("https://www.flipkart.com/")
#     browser.find_element(By.XPATH, "//button[text()='✕']").click()
#     browser.find_element(By.XPATH, "//input[@placeholder='Search for products, brands and more']").send_keys(
#         "fastrack watch")
#     browser.find_element(By.XPATH,"//button[@type='submit']").click()
#     time.sleep(5)
#     tlt =browser.title
#     print(tlt)


sentence = "the boy has a pen the pen has a cap the the"
words = sentence.split()
count = 0
for word in words:
    if word == 'the':
        count += 1
print("the word 'the ' appears", count, "times in the scentence.")
