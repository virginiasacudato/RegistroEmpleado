from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.Home import Home
import time


class TestHome(WebDriverSetup):

    def test_a_gen_employee(self):
        driver = self.driver
        home = Home(driver)
        home.gen_employ()
        time.sleep(4)
