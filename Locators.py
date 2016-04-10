from selenium.webdriver.common.by import By


class MainPageLocators(object):
    HEADER = (By.ID, "logo")
    CURRENCYLIST  = (By.ID, "currency")
    CURRENCY      = (By.NAME, "GBP")
    SEARCHINPUT = (By.NAME, "search")
    SEARCHBUTTON = (By.XPATH, ".//*[@id='search']/span/button")
    CURRENCYTOCHECK = (By.TAG_NAME, "strong")


class SearchResultPagePageLocators(object):
    CARTSTOADD = (By.XPATH,"//*[contains(@data-original-title, 'Compare this Product')]")
    LISTVIEW = (By.XPATH, ".//*[@id='list-view']")
    COMPARELINK = (By.XPATH, ".//*[@id='compare-total']")


class ProductComparisonPageLocators (object):

    SHOPPINGCARTLINK = (By.LINK_TEXT, "shopping cart")

class ShoppingCartLocators (object):
    TOTALPRICE = (By.XPATH, ".//*[@id='content']/form/div/table/tbody/tr/td[6]")
