from base.base_schema import BaseSchema


class HospitalGet(BaseSchema):
    id: int
    name: str
    address: str
    phone: str
    lat: float
    lon: float

class HospitalCreate(BaseSchema):
    name: str
    address: str
    phone: str
