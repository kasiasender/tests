from base import Page
from Locators import *
from time import sleep
import random



class MainPage(Page):

    def check_page_loaded(self):
        return self.find_element(*MainPageLocators.HEADER)

    def choose_currency(self):
        self.find_element(*MainPageLocators.CURRENCYLIST).click()
        self.find_element(*MainPageLocators.CURRENCY).click()
        return self.find_element(*MainPageLocators.CURRENCYTOCHECK)


    def enter_search_term(self, search):
        searchinput = self.find_element(*MainPageLocators.SEARCHINPUT)
        searchbutton = self.find_element(*MainPageLocators.SEARCHBUTTON)
        searchinput.clear()
        searchinput.send_keys(search)
        sleep(1)
        searchbutton.click()

        results_search_bar = self.wait_for_element(*MainPageLocators.SEARCHINPUT)
        return results_search_bar.get_attribute('value') == search


class SearchResultPage(Page):

    def add_to_comparasion(self):
        addToCarts = self.find_elements(*SearchResultPagePageLocators.CARTSTOADD)
        numFoElem = 0
        for cart in addToCarts:
            cart.click()
            numFoElem += 1
        self.find_element(*SearchResultPagePageLocators.LISTVIEW).click()
        self.find_element(*SearchResultPagePageLocators.COMPARELINK).click()
        return numFoElem


class ProductComparisonPage(Page):


    def remove_product_avability(self,avability,numOfElem):

        col_min = 2
        col_max = numOfElem + 2

        while col_min < col_max:
            element = self.driver.find_element_by_xpath(".//*[@id='content']/table/tbody[1]/tr[6]/td[" + str(col_min) + "]")
            if element.text == avability:
                self.driver.find_element_by_xpath((".//*[@id='content']/table/tbody[2]/tr/td[" + str(col_min) + "]/a")).click()
                col_max -= 1
                col_min -= 1
            col_min += 1
        numFoElem = col_max - 2

        rand = random.randint(2, numFoElem + 1)


        cena = self.driver.find_element_by_xpath(".//*[@id='content']/table/tbody[1]/tr[3]/td[" + str(rand) + "]")
        cena = cena.text
        for char in cena:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                cena = cena.replace(char, '')
        cena = float(cena)

        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath(".//*[@id='content']/table/tbody[2]/tr/td[" + str(rand) + "]/input").click()

        self.find_element(*ProductComparisonPageLocators.SHOPPINGCARTLINK).click()
        return cena

class ShoppingCart(Page):

    def Total_price(self):

        totalPrice = self.find_element(*ShoppingCartLocators.TOTALPRICE).text

        for char in totalPrice:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                totalPrice = totalPrice.replace(char, '')
        totalPrice = float(totalPrice)
        return totalPrice









