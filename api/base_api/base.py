import logging
from unittest import TestCase

from selenium import webdriver

import settings

# driver = webdriver.PhantomJS()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
logger = logging.getLogger(__name__)


class BaseSeleniumTestCase(TestCase):
    def get_web_driver(self):
        driver = webdriver.Chrome(
            executable_path=settings.GECKODRIVER_PATH)
        driver.set_window_size(1400, 1000)
        return driver

    def setUp(self):
        self.selenium = self.get_web_driver()

    def tearDown(self):
        self.selenium.quit()
        pass
