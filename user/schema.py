from base.base_schema import BaseSchema


class UserGet(BaseSchema):
    id : int
    nama : str
    email : str

class UserCreate(BaseSchema):
    name : str
    nif: str
    email : str
    password : str