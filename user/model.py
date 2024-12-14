from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String
from base.StrEnum import StrEnum
from base.base_model import BaseModel

class UserType(Enum):
    USER = "USER"
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

class User(BaseModel):
    __tablename__ = "m_user"
    id: int = Column(Integer, primary_key=True, index=True)
    nif: str = Column(String, unique=True, index=True)
    name: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
    is_active: bool = Column(Boolean, default=True)
    type: UserType = Column(StrEnum(UserType))
    
    __mapper_args__ = {
        "polymorphic_identity": UserType.USER,
        "polymorphic_on": type,
    }
