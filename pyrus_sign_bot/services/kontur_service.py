import requests
from base64 import b64encode


class KonturService:
    """
    Класс для работы с `Контур API`
    """

    def __init__(self):
        pass

    def login(self):
        s = requests.Session()
        s.headers['Host'] = 'identity.kontur.ru'
        s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows; Windows NT 6.3;; en-US) AppleWebKit/601.48 (KHTML, like Gecko) Chrome/54.0.2253.359 Safari/601'

        pass
