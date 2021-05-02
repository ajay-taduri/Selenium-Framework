from selenium import webdriver


class Testdata():
    application_url = "http://localhost/invoice/app/index.php?signIn=1"
    userId = "admin"
    password = "admin"

class Basepage():
    def __init__(self, driver):
        self.driver = driver

class Testbase():
    def setup(self):
        self.driver = webdriver.chrome()
        self.driver.maximize()






