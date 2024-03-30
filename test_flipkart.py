import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  EC
import time
# driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.mark.usefixtures("setUp")
class TestFlipart:
    def test_assert_title(self):
        print("EXECUTING THE FIRST TESSTT ________")
        driver = self.driver
        title = driver.title
        assert title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        driver.maximize_window()

    def test_search_box(self):
        print("EXECUTING THE SECOND TESSTT ________")
        search_box = self.driver.find_element_by_css_selector("input[name='q']")
        search_box.send_keys("laptop")
        data = search_box.get_attribute('value')
        print(data)

    def test_select_laptop(self):
        global wait
        wait = WebDriverWait(self.driver, 10)
        options = wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,"li[class='_3D0G9a']")))
        for option in options:
            if option.text =='laptop bag':
                option.click()
                break

    def test_select_price_range(self):
        global action
        action = ActionChains(self.driver)
        source = self.driver.find_element_by_css_selector("div[class='_31Kbhn _28DFQy']")
        target = self.driver.find_element_by_css_selector("div[class='_1ftpgI']:nth-child(2)")
        time.sleep(2)
        action.drag_and_drop(source,target).perform()


    def test_navigate_to_mainpage(self):
        self.driver.find_element_by_css_selector("div[class='_3qX0zy']").click()

    def test_hover_on_the_options(self):
        actions = ActionChains(self.driver)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(), 'Fashion')]")))
        self.driver.find_element_by_xpath("//span[contains(text(), 'Fashion')]").click()
        time.sleep(2)
        womenswear = self.driver.find_element_by_link_text("Men's Bottom Wear")
        # finaloption= self.driver.find_element_by_xpath("//a[contains(text(), \"Men's Trousers\")]")
        time.sleep(2)
        actions.move_to_element(womenswear).perform()


