from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global driver,product
    product = input("Enter the product to searched :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_searchProducts(setUp):
    driver.get("https://www.flipkart.com/")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    driver.find_element_by_name("q").send_keys(product)
    driver.find_element_by_class_name("LOZ3Pu").click()