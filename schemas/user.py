from pydantic import BaseModel, validator
from validate_email import validate_email
from enums.global_enams import Gender, Status, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @validator('email')
    def email_address_verification(cls, email):
        if validate_email(email):
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
