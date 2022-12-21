import requests

from enums.global_enams import GlobalErrorMassage


class Response:
    def __init__(self, response):
        self.response = response

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

    def assert_post_count(self, count, data=None):
        assert len(self.response.json().get(data)) == count, GlobalErrorMassage.WRONG_ELEMENT_COUNT.value
