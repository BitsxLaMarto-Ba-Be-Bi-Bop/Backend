from base.base_service import BaseService
from hospital.model import Hospital


class HospitalService(BaseService):
    name = 'hospital_service'
    __model__ = Hospital
