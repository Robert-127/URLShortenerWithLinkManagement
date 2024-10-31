import requests

class URLShortener:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://api-ssl.bitly.com/v4"

