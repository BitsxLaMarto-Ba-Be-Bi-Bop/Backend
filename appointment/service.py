from fastapi_sqlalchemy import db
from appointment.model import Appointment
from base.base_service import BaseService


class AppointmentService(BaseService):
    name = 'appointment_service'
    __model__ = Appointment

    def accept_appointment(self, appointment_id: int):
        appointment:Appointment = self.get_by_id(appointment_id)
        appointment.doctor_acception = True
        self.update(appointment)
        return appointment
    

    def get_mine(self, patient_id: int):
        return db.session.query(Appointment).filter(Appointment.patient_id == patient_id).all()