from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, foreign
from user.model import User, UserType
if TYPE_CHECKING:
    from user_doctor.model import UserDoctor


class UserPatient(User):
    __tablename__ = 'user_patient'
    id: int = Column(Integer, ForeignKey("m_user.id"), primary_key=True)
    birtdate: date = Column(Date, nullable=False)
    gender: str = Column(String, nullable=False)
    tobaco: bool = Column(Boolean, nullable=False)
    tratment: str = Column(String)
    pills: str = Column(String)
    blood_type: str = Column(String, nullable=False)
    preceding_person: str = Column(String)
    preceding_illnes: str = Column(String)
    alergies: str = Column(String)
    weight: float = Column(Float, nullable=False)
    height: float = Column(Float, nullable=False)
    
    doctors: list["UserDoctor"] = relationship("UserDoctor", secondary="trates", back_populates="patients", primaryjoin="and_(UserPatient.id==Trates.patient_id)")
    
    __mapper_args__ = {
        "polymorphic_identity": UserType.PATIENT,
        # 'with_polymorphic': '*'
    }