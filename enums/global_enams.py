from enum import Enum


class GlobalErrorMassage(Enum):
    WRONG_STATUS_CODE = 'Received status code is not to equal to expected.'
    WRONG_ELEMENT_COUNT = 'Number of items is not to equal to expected.'