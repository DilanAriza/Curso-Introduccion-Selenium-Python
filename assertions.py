import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    
    # Selectores con test
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"./geckodriver.exe")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))    

    def test_language_options(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by= how, value= what)
        except NoSuchElementException as variable:
            return False
        
        return True

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
    )