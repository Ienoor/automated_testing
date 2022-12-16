import requests

from enums.global_enams import GlobalErrorMassage


class Response:
    def __init__(self, url, data=None):
        self.data = data
        if self.data is None:
            self.response = requests.get(url)
        else:
            self.response = requests.get(url)

    def validate_data(self, schema, data=None):
        if data is None:
            if isinstance(self.response.json(), list):
                for item in self.response.json():
                    schema.parse_obj(item)
            else:
                schema.parse_obj(self.response.json())
        else:
            if isinstance(self.response.json().get(data), list):
                for item in self.response.json().get(data):
                    schema.parse_obj(item)
            else:
                schema.parse_obj(self.response.json().get(data))

    def assert_status_code(self, code):
        if isinstance(code, list):
            assert self.response.status_code in code, GlobalErrorMassage.WRONG_STATUS_CODE.value
        else:
            assert self.response.status_code == code, GlobalErrorMassage.WRONG_STATUS_CODE.value

    def assert_post_count(self, count):
        assert len(self.response.json()) == count, GlobalErrorMassage.WRONG_ELEMENT_COUNT.value
