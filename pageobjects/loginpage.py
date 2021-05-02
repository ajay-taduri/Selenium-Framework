from resources.testdata import Basepage, Testdata


class Login(Basepage):

    def __init__(self, driver):
        super.__init__(driver)
        self.driver.get(Testdata.application_url)