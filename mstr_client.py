import requests

from config import settings


class MSTRClient:
    def __init__(self):
        self.base_url = settings.MSTR_BASE_URL
        self.verify_ssl = settings.VERIFY_SSL

        self.session = requests.Session()
        self.session.verify = self.verify_ssl

        self.auth_token = None

    def set_auth_token(self, token):
        self.auth_token = token
        self.session.headers.update({
            "X-MSTR-AuthToken": token
        })

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)

    def post(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, **kwargs)

    def put(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, **kwargs)

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)