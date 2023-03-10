import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture
def get_users():
    return requests.get(SERVICE_URL)
