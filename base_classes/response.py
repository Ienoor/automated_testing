import requests
from jsonschema import validate

from enums.global_enams import GlobalErrorMassage


class Response:
    def __init__(self, url):
        self.response = requests.get(url)

    def validate_data(self, schema):
        if isinstance(self.response.json(), list):
            for item in self.response.json():
                validate(item, schema)
        else:
            validate(self.response, schema)

    def assert_status_code(self, code):
        if isinstance(code, list):
            assert self.response.status_code in code, GlobalErrorMassage.WRONG_STATUS_CODE.value
        else:
            assert self.response.status_code == code, GlobalErrorMassage.WRONG_STATUS_CODE.value

    def assert_post_count(self, count):
        assert len(self.response.json()) == count, GlobalErrorMassage.WRONG_ELEMENT_COUNT.value
