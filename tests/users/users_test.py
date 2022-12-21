import pytest

from Classes.response import Response
from schemas.user import User


@pytest.mark.production
def test_data_validation(get_users):
    Response(get_users).validate_data(User, 'data')


@pytest.mark.skip
def test_user_count(get_users, count=10):
    Response(get_users).assert_post_count(count, 'data')
