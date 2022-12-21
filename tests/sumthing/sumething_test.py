from Classes.response import Response


def test_getting_code_status(get_users):
    Response(get_users).assert_status_code(200)


def test_post_count(get_users, count=10):
    Response(get_users).assert_post_count(count, 'data')

