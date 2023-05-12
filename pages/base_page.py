import os

from utils.selenium_wrapper import SeleniumWrapper


class BasePage(SeleniumWrapper):
    UI_URL = "https://habr.com/"
    baseurl = os.environ.get("UI_URL", UI_URL)
