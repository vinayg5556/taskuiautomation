import time
from Base.ActionsPage import ActionPage


class Search_mobile(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_TB = "//input[@id='twotabsearchtextbox']"
    search_BTN = "//input[@id='nav-search-submit-button']"
    logo_BTN = "//a[@id='nav-logo-sprites']"
    pagination = "//*[@class='a-section a-text-center s-pagination-container']"  # to scroll window to pagination container
    page_number_class_name = "//*[@class='s-pagination-item s-pagination-button']"  # number before 5
    pagination_number = "//*[@class='s-pagination-item s-pagination-button'][3]"  # number after 5
    first_item_inPage = "//*[@data-index =2]//following-sibling::h2/a"
    product_title = "//*[@id = 'title_feature_div']//span[@id='productTitle']"
    # _ratingCount = "//*[@id='averageCustomerReviews_feature_div']//*[@id = 'acrCustomerReviewLink']/span"  # textContent
    price_data = "//div[contains(@class, 'none aok-align-center')]//span[contains(@class, 'a-price aok-align')]//span[@class='a-price-whole']"  # textContent

    def get_mobile_data(self):
        productName = self.getText(self.product_title, "XPATH", "textContent")
        time.sleep(1)
        # productRating = self.getText(self._ratingCount, "XPATH", "textContent")
        # time.sleep(1)
        productPrice = self.getText(self.price_data, "XPATH", "textContent")
        print(
            f"Found product data with name as :: {productName} and with price {productPrice}")
        self.log.info(f"Found product data with name as :: {productName} and with price {productPrice}")

    def search_mobile(self):
        self.click(self.logo_BTN, "XPATH")
        self.sendKeys(self.search_TB, "XPATH", "mobiles")
        self.click(self.search_BTN, "XPATH")
        time.sleep(2)
        for i in range(2, 16):
            self.click(self.first_item_inPage, "XPATH")
            time.sleep(10)
            self.moveToCurrentTab(1)
            time.sleep(2)
            self.get_mobile_data()
            time.sleep(3)
            self.closeTab()
            self.moveToCurrentTab(0)
            time.sleep(2)
            self.moveToElement(self.pagination)
            time.sleep(3)
            if i < 6:
                self.clickOnIndex(self.page_number_class_name, "XPATH", i - 1)
            else:
                self.click(self.pagination_number, "XPATH")
            time.sleep(3)
