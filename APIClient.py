# -*- coding: UTF-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth


class APIClient:
    def __init__(self, login=None, password=None, data=None, count=None):
        self.url = 'https://service.modulpos.ru/api/v1/retail-points'
        self.login = login
        self.password = password
        self.auth = HTTPBasicAuth(self.login, self.password)
        self.headers = {'content-type': 'application/json', 'charset': 'UTF-8'}
        self.data = data
        self.count = count

    def retail_points(self):
        re = requests.post(url=self.url, headers=self.headers, data=json.dumps(self.data), auth=self.auth)
        return re

    def retail_point_update(self):
        re = requests.put(url='https://service.modulpos.ru/api/v1/retail-point/{count}'.format(count=self.count),
                          auth=self.auth, data=json.dumps(self.data), headers=self.headers)
        return re
