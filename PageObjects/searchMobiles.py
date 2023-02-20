import time
from Base.ActionsPage import Action_page


class Search_mobile(Action_page):

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
        productName = self.get_text(self.product_title, "XPATH", "textContent")
        time.sleep(1)
        # productRating = self.getText(self._ratingCount, "XPATH", "textContent")
        # time.sleep(1)
        productPrice = self.get_text(self.price_data, "XPATH", "textContent")
        print(
            f"Found product data with name as :: {productName} and with price {productPrice}")
        self.log.info(f"Found product data with name as :: {productName} and with price {productPrice}")

    def search_mobile(self):
        self.click(self.logo_BTN, "XPATH")
        self.send_keys(self.search_TB, "XPATH", "mobiles")
        self.click(self.search_BTN, "XPATH")
        time.sleep(2)
        for i in range(2, 16):
            self.click(self.first_item_inPage, "XPATH")
            time.sleep(5)
            self.move_to_current_tab(1)
            self.get_mobile_data()
            self.close_tab()
            self.move_to_current_tab(0)
            self.move_to_the_element(self.pagination)
            time.sleep(3)
            if i < 6:
                self.click_on_index(self.page_number_class_name, "XPATH", i - 1)
            else:
                self.click(self.pagination_number, "XPATH")
