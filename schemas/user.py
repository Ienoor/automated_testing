from pydantic import BaseModel

from enums.global_enams import Gender, Status


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status
