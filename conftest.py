from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest



@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    driver.get("https://www.flipkart.com/")


    yield driver
    driver.quit()
