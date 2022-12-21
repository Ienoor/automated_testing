from Classes.response import Response
from schemas.user import User


def test_data_validation(get_users):
    Response(get_users).validate_data(User, 'data')
