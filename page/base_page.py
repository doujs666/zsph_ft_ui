# coding=UTF-8
import logging,os,settings
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from settings import WAIT_TIME

logger = logging.getLogger(__name__)


def fail_on_screenshot(function):
    def get_snapshot_directory():
        if not os.path.exists(settings.SNAPSHOT_DIRECTORY):
            os.mkdir(settings.SNAPSHOT_DIRECTORY)
        return settings.SNAPSHOT_DIRECTORY

    def get_current_time_str():
        return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")

    def wrapper(*args, **kwargs):
        instance, selector = args[0], args[1]
        try:
            return function(*args, **kwargs)
        except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
            logger.error("Could not find the selector: [{}].".format(selector))
            filename = "{}.png".format(get_current_time_str())
            screenshot_path = os.path.join(get_snapshot_directory(), filename)
            logger.debug(instance.selenium.page_source)
            instance.selenium.save_screenshot(screenshot_path)
            raise ex
    return wrapper


class BasePage(object):
    url = ""
    base_url = settings.WEB_TEST_BASE_URL

    def __init__(self, selenium, url_params=None):
        if not url_params:
            url_params = []
        self.selenium = selenium
        self.url_params = url_params
        self.go_to()

    def go_to(self):
        logger.debug("Goto page: [{}]".format(self.get_page_url()))
        return self._selenium_get_url(self.get_page_url())

    def refresh(self):
        self.selenium.refresh()

    def navigate_back(self):
        self.selenium.back()

    def _selenium_get_url(self, url):
        try:
            self.selenium.get('about:blank')
            self.selenium.get(str(url))
        except Exception as ex:
            logger.error("Can not open the url:[{}]".format(url))
            raise ex
        return self

    def get_page_url(self):
        if not self.url:
            raise RuntimeError("no url been set")
        return self._get_url(self.url)

    def _get_url(self, url):
        format_url = url.format(*self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    def get_current_page_url(self):
        return self.selenium.current_url

    def get_page_title(self):
        return self.selenium.title

    def get_cookie_value(self):
        return self.selenium.get_cookie('client_identity')['value']

    def get_current_window_handle(self):
        return self.selenium.current_window_handle

    def get_window_handles(self):
        return self.selenium.window_handles

    def choose_window_handle(self, handle):
        self.selenium.switch_to.window(handle)
        return self

    # 刷新页面
    def refresh_page(self):
        self.selenium.refresh()
        return self

    # 控制js
    def execute_script(self):
        js = "window.scrollTo(0,0)"
        self.selenium.execute_script(js)

    # ---------------------------------------------------------------------------------------------------------------
    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

    @fail_on_screenshot
    def find_element_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_element_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_partial_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def find_element_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def find_element_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def find_element_by_class_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def find_element_by_tag_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.TAG_NAME, selector)))

    # ----------------------------------------------------------------------------------------------------------------
    '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

    @fail_on_screenshot
    def find_elements_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_elements_by_class_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def find_elements_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_elements_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.XPATH, selector)))

    @fail_on_screenshot
    def find_elements_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.presence_of_all_elements_located((By.NAME, selector)))

    # -------------------------------------------------------------------------------------------------------------
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''

    @fail_on_screenshot
    def invisible_element_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def invisible_element_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def invisible_element_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def invisible_element_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def invisible_element_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_class_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_tag_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.TAG_NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_partial_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.invisibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

    @fail_on_screenshot
    def text_to_be_present_in_element_by_id(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.ID, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_class_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.CLASS_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_xpath(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.XPATH, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_tag_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.TAG_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_css(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element((By.CSS_SELECTOR, selector),text))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_css(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.CSS_SELECTOR, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_id(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.ID, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_css_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.CLASS_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_xpath(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.XPATH, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_tag_name(self, selector, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.text_to_be_present_in_element_value((By.TAG_NAME, selector),text))


    # -----------------------------------------------------------------------------------------------------------------
    '''判断title,返回布尔值'''

    @fail_on_screenshot
    def page_title_is(self, title, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(expected.title_is(title))

    @fail_on_screenshot
    def page_title_contains(self, title, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(expected.title_contains(title))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断某个元素中是否可见并且是enable的，代表可点击'''

    @fail_on_screenshot
    def element_to_be_click_able_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.ID, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_class_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_tag_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.TAG_NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.XPATH, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_link_text(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.element_to_be_clickable((By.LINK_TEXT, selector)))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断元素是否可见，如果可见就返回这个元素，不可见返回False'''

    @fail_on_screenshot
    def visibility_of_element_by_id(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_class_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_css(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_xpath(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_tag_name(self, selector, wait_time=WAIT_TIME):
        return WebDriverWait(self.selenium, wait_time).until(
            expected.visibility_of_element_located((By.TAG_NAME, selector)))

    def get_cookie_by_name(self, name):
        cookie = self.selenium.get_cookie(name)
        return cookie['value']

    def get_session_id(self):
        return self.get_cookie_by_name("TSID")


class UserBasePage(BasePage):
    base_url = settings.WEB_TEST_BASE_URL