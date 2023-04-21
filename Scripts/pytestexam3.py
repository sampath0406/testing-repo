import  pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield
    driver.close()
def test_login(setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    assert driver.title == "OrangeHRM"
def test_invalidlogin(setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME,"username").send_keys("admin")
    driver.find_element(By.NAME,"password").send_keys("admin113")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    assert "invalid credentials" in driver.page_source

