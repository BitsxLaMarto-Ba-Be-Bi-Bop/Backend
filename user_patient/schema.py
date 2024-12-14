from datetime import date
from user.schema import UserCreate, UserGet


class UserPatientCreate(UserCreate):
    birtdate: date
    gender: str
    tobaco: bool
    tratment: str
    pills: str
    blood_type: str
    preceding_person: str
    preceding_illnes: str
    alergies: str
    weight: float 
    height: float 

class UserPatientGet(UserGet):
    birtdate: date
    gender: str
    tobaco: bool
    tratment: str
    pills: str
    blood_type: str
    preceding_person: str
    preceding_illnes: str
    alergies: str
    weight: float 
    height: float 

class UserPatientGetAll(UserGet):
    pass