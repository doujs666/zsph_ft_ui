import logging
from unittest import TestCase
from pytesser3 import *
from PIL import Image
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
        driver = webdriver.Firefox(executable_path=settings.GECKODRIVER_PATH)
        driver.set_window_size(1400, 1000)
        return driver

    # def get_web_driver(self):
    #     driver = webdriver.Firefox(
    #         executable_path=settings.GECKODRIVER_PATH) if settings.ENV == "dev" else webdriver.PhantomJS()
    #     driver.set_window_size(1400, 1000)
    #     return driver

    def setUp(self):
        self.selenium = self.get_web_driver()

    def tearDown(self):
        self.selenium.quit()
        pass


class ImageCaptcha(object):

    def get_image_captcha(self, file_path):

        img = Image.open(file_path)
        img_grey = img.convert('L')
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # img_out = img_grey.point(table, '1')
        image_text = image_to_string(img_grey)
        return image_text
