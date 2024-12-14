from fastapi import HTTPException
from fastapi_sqlalchemy import db
from base.base_service import BaseService
from user.model import User
from user_doctor.model import Trates, UserDoctor
from user_doctor.schema import UserDoctorCreate
from user_patient.model import UserPatient
from user_patient.schema import UserPatientCreate


class UserService(BaseService):
    name = 'user_service'
    __model__ = User

    def get_by_mail(self, mail: str):
        return db.session.query(self.__model__).filter(self.__model__.email == mail).first()

    def register_doctor(self,payload: UserDoctorCreate):
        doctor = UserDoctor(**payload.model_dump(exclude={'password'}))
        # Hash the password
        doctor.hashed_password = self.get_password_hash(payload.password)
        db.session.add(doctor)
        db.session.commit()
        return doctor
    
    def register_patient(self,payload: UserPatientCreate):
        doctor = UserPatient(**payload.model_dump(exclude={'password'}))
        # Hash the password
        doctor.hashed_password = self.get_password_hash(payload.password)
        db.session.add(doctor)
        db.session.commit()
        return doctor
    
    def get_untrated_paients(self):
        patient_ids = db.session.query(Trates.patient_id).all()
        untrated_patients = db.session.query(UserPatient).filter(UserPatient.id.notin_(patient_ids)).all()
        return untrated_patients
    
    def get_trated_paients(self, docter_id:int):
        doctor = db.session.query(UserDoctor).get(docter_id)
        if not doctor:
            raise HTTPException(status_code=404,detail='Doctor not found')
        trated_patients = doctor.patients
        return trated_patients
    
    def get_doctors(self):
        doctors = db.session.query(UserDoctor).all()
        return doctors

    def asign_patient_to_doctor(self,doctor_id:int,patient_id:int):
        doctor:UserDoctor = db.session.query(UserDoctor).get(doctor_id)
        patient = db.session.query(UserPatient).get(patient_id)
        if not doctor or not patient:
            raise HTTPException(status_code=404,detail='Doctor or Patient not found')
        if patient in doctor.patients:
            raise HTTPException(status_code=400,detail='Patient already assigned to doctor')
        doctor.patients.append(patient)
        db.session.commit()
        return doctor