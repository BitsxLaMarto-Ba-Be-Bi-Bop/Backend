from datetime import datetime

from base.base_schema import BaseSchema


class AppointmentCreate(BaseSchema):
    doctor_id: int
    patient_id: int
    appointment_date: datetime

class AppointmentGet(BaseSchema):
    doctor_id: int
    patient_id: int
    appointment_date: datetime