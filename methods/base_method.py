from abc import ABC

import requests


class BaseMethod(ABC):

    def post(self, *, url, payload, headers):
        response = requests.post(
            url=url,
            data=payload, 
            headers=headers
        )
        return response
