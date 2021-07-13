import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"./geckodriver.exe")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://google.com/")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
    )