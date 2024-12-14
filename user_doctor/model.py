from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from base.base_model import BaseModel
from user.model import User, UserType
from user_patient.model import UserPatient


class UserDoctor(User):
    # __tablename__ = 'user_doctor'
    # id: int = Column(ForeignKey('m_user.id'), primary_key=True)
    patients: list["UserPatient"] = relationship("UserPatient", secondary="trates", back_populates="doctors")
    __mapper_args__ = {
        "polymorphic_identity": UserType.DOCTOR,
        # 'with_polymorphic': '*'
    }
class Trates(BaseModel):
    __tablename__ = 'trates'
    user_doctor_id = Column(Integer, ForeignKey('user_doctor.id'), primary_key=True)
    user_pacient_id = Column(Integer, ForeignKey('user_pacient.id'), primary_key=True)