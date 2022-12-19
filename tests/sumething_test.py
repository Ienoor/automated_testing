from base_classes.response import Response
from configuration import SERVICE_URL
from schemas.user import User


def test_getting_code_status():
    Response(SERVICE_URL).assert_status_code(200)


def test_post_count(count=10):
    Response(SERVICE_URL).assert_post_count(count, 'data')


def test_data_validation():
    Response(SERVICE_URL).validate_data(User, 'data')
