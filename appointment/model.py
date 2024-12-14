from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from base.base_model import BaseModel

class Appointment(BaseModel):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("user_doctor.id"))
    patient_id = Column(Integer, ForeignKey("user_patient.id"))

    doctor_acception = Column(Boolean, nullable=False, default=False)
    appointment_date = Column(DateTime, nullable=False)
    reason: str = Column(String, nullable=False)
    doctor = relationship("UserDoctor", foreign_keys=[doctor_id])
    patient = relationship("UserPatient", foreign_keys=[patient_id])

    @property
    def doctor_name(self):
        return self.doctor.name