from fastapi import APIRouter, Depends, HTTPException
from base.base_token import BaseToken
from base.jwt_bearer import JWTBearer
from user.schema import UserCreate
from user.service import UserService
from user_doctor.schema import UserDoctorCreate
from user_patient.schema import UserPatientCreate


router = APIRouter()
user_service = UserService()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
def create_user(user: UserCreate):
    new_user = user_service.create(user)
    return new_user

@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, token:BaseToken=Depends(JWTBearer())):
    updated_user = user_service.update(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, token:BaseToken=Depends(JWTBearer())):
    deleted = user_service.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}


@router.post("/users/doctors")
def register_doctor(doctor: UserDoctorCreate):
    new_doctor = user_service.register_doctor(doctor)
    return new_doctor

@router.post("/users/patients")
def register_patient(patient: UserPatientCreate):
    new_patient = user_service.register_patient(patient)
    return new_patient

@router.get("/users/patients/untrated")
def get_untrated_patients(token:BaseToken=Depends(JWTBearer())):
    untrated_patients = user_service.get_untrated_paients()
    return untrated_patients

@router.get("/users/patients/trated/{doctor_id}")
def get_trated_patients(doctor_id: int, token:BaseToken=Depends(JWTBearer())):
    trated_patients = user_service.get_trated_paients(doctor_id)
    return trated_patients

@router.get("/users/doctors/")
def get_doctors(token:BaseToken=Depends(JWTBearer())):
    doctors = user_service.get_doctors()
    return doctors

@router.post("/users/doctors/{doctor_id}/patients/{patient_id}")
def asign_patient_to_doctor(doctor_id: int, patient_id: int, token:BaseToken=Depends(JWTBearer())):
    doctor = user_service.asign_patient_to_doctor(doctor_id, patient_id)
    return doctor
