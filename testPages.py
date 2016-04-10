#-*- coding: utf-8 -*-

import unittest
from Pages import *
from selenium import webdriver


class TestPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://demo.opencart.com/")

    def test_check_price(self):

        main_page = MainPage(self.driver)
        self.assertTrue(main_page.check_page_loaded())

        search_result_page = SearchResultPage(self.driver)
        product_comparision_page = ProductComparisonPage(self.driver)
        shopping_cart = ShoppingCart(self.driver)

        currency = main_page.choose_currency()
        self.assertEquals(currency.text,u"£")

        search = main_page.enter_search_term("ipod")
        self.assertTrue(search)

        num_of_elements = search_result_page.add_to_comparasion()

        cena = product_comparision_page.remove_product_avability("Out Of Stock",num_of_elements)
        total_price = shopping_cart.Total_price()

        self.assertEquals(cena,total_price)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
