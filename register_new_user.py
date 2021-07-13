import unittest
from selenium import webdriver
import time

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"./geckodriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(7)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Register').click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_susbcription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        password_confirm = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_susbcription.is_enabled()
        and password.is_enabled()
        and password_confirm.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Test')
        driver.implicitly_wait(2)
        middle_name.send_keys('Test')
        driver.implicitly_wait(2)
        last_name.send_keys('Test')
        driver.implicitly_wait(2)
        email_address.send_keys('test@testingmail.com')
        driver.implicitly_wait(2)
        password.send_keys('Test')
        driver.implicitly_wait(2)
        password_confirm.send_keys('Test')
        driver.implicitly_wait(2)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
    )