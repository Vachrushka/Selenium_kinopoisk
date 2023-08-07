from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def getWait(self, delay):
        return WebDriverWait(self.driver, delay)
