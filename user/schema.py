from base.base_schema import BaseSchema


class UserGet(BaseSchema):
    id : int
    nama : str
    email : str

class UserCreate(BaseSchema):
    nama : str
    email : str
    password : str