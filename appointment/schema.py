from datetime import datetime

from base.base_schema import BaseSchema


class AppointmentCreate(BaseSchema):
    doctor_id: int
    patient_id: int
    appointment_date: datetime
    reason:str
    doctor_acception: bool = False

class AppointmentGet(BaseSchema):
    doctor_id: int
    patient_id: int
    appointment_date: datetime
    reason:str
    doctor_name: str