from base_classes.response import Response
from configuration import SERVICE_URL
from schemas.post import Post


def test_getting_code_status():
    Response(SERVICE_URL).assert_status_code(200)


def test_post_count():
    Response(SERVICE_URL).assert_post_count(3)


def test_data_validation():
    Response(SERVICE_URL).validate_data(Post)
