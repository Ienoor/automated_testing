from enum import Enum


class GlobalErrorMassage(Enum):
    WRONG_STATUS_CODE = 'Received status code is not to equal to expected.'
    WRONG_ELEMENT_COUNT = 'Number of items is not to equal to expected.'


class Gender(Enum):
    FEMALE = 'female'
    MALE = 'male'


class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain"
