from appointment.model import Appointment
from base.base_service import BaseService


class AppointmentService(BaseService):
    name = 'appointment_service'
    __model__ = Appointment

    def accept_appointment(self, appointment_id: int):
        appointment = self.get_by_id(appointment_id)
        appointment.is_accepted = True
        self.update(appointment)
        return appointment