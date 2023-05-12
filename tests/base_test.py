import os


class BaseTest:
    UI_URL = "https://habr.com/"
    baseurl = os.environ.get("UI_URL", UI_URL)
