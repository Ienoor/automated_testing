import pytest
import requests

from configuration import SERVICE_URL


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b


@pytest.fixture
def calculate():
    return _calculate
