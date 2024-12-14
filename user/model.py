from enum import Enum
from sqlalchemy import Column
from base.StrEnum import StrEnum
from base.base_model import BaseModel

class UserType(Enum):
    USER = "USER"
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

class User(BaseModel):
    __tablename__ = "m_user"
    id: int = Column(primary_key=True, index=True)
    nif: str = Column(unique=True, index=True)
    name: str = Column(unique=True, index=True)
    email: str = Column(unique=True, index=True)
    hashed_password: str = Column()
    is_active: bool = Column(default=True)
    type: UserType = Column(StrEnum(UserType))
    
    __mapper_args__ = {
        # "polymorphic_identity": UserType.USER,
        "polymorphic_on": type,
    }
