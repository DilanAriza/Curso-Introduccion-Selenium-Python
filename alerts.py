import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"./geckodriver.exe")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alert(self):
        driver = self.driver
        
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/ul/li[2]/a').click()

        driver.find_element_by_link_text('Clear All').click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
    )