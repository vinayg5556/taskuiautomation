import time
from Base.ActionsPage import ActionPage


class searchMobile(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_TB = "//input[@id='twotabsearchtextbox']"
    _search_BTN = "//input[@id='nav-search-submit-button']"
    _logo_BTN = "//a[@id='nav-logo-sprites']"
    _pagination = "//*[@class='a-section a-text-center s-pagination-container']"  # to scroll window to pagination container
    _pageNumber_className = "//*[@class='s-pagination-item s-pagination-button']"  # number before 5
    _pagination_number = "//*[@class='s-pagination-item s-pagination-button'][3]"  # number after 5
    _first_item_inPage = "//*[@class='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16'][1]//div[2]//*[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style']//h2/a"
    _productTitle = "//*[@id = 'title_feature_div']//span[@id='productTitle']"
    _ratingCount = "//*[@id='averageCustomerReviews_feature_div']//*[@id = 'acrCustomerReviewLink']/span"  # textContent
    _priceData = "//*[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[2]/span[2]"  # textContent

    def get_mobileData(self):
        productName = self.getText(self._productTitle, "XPATH", "textContent")
        time.sleep(1)
        productRating = self.getText(self._ratingCount, "XPATH", "textContent")
        time.sleep(1)
        productPrice = self.getText(self._priceData, "XPATH", "textContent")
        print(
            f"Found product data with name as :: {productName} and with price {productPrice} and with rating as {productRating}")
        self.log.info(f"Found product data with name as :: {productName} and with price {productPrice} and with rating as {productRating}")

    def searchMobile(self):
        self.click(self._logo_BTN, "XPATH")
        self.sendKeys(self._search_TB, "XPATH", "mobiles")
        self.click(self._search_BTN, "XPATH")
        time.sleep(2)
        for i in range(2, 16):
            self.click(self._first_item_inPage, "XPATH")
            time.sleep(10)
            self.moveToCurrentTab(1)
            time.sleep(2)
            self.get_mobileData()
            time.sleep(3)
            self.closeTab()
            self.moveToCurrentTab(0)
            time.sleep(2)
            self.moveToElement(self._pagination)
            time.sleep(3)
            if i < 6:
                self.clickOnIndex(self._pageNumber_className, "XPATH", i - 1)
            else:
                self.click(self._pagination_number, "XPATH")
            time.sleep(3)
