from logging import setLogRecordFactory
import unittest
from selenium import webdriver
from termcolor import colored

class HomePageTest(unittest.TestCase):
    
    # Selectores con test
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = r"./geckodriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
        print(colored("Se encontro la caja de busqueda", "green"))

    def test_search_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
        print(colored("Se encontro la caja de busqueda", "green"))
    
    def test_search_field_by_class(self):
        search_field = self.driver.find_element_by_class_name("input-text")
        print(colored("Se encontro la caja de busqueda", "green"))

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
        print(colored("Se encontro el boton de busqueda", "green"))

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img");
        self.assertEqual(3, len(banners))
        print(colored("Si existen los 3 banners de promos", "green"))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
        print(colored("Se encontro la imagen principal del carrusel", "green"))

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        print(colored("Se encontro el carrito de compras", "green"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
    )