
from fastapi import APIRouter, Depends

from appointment.schema import AppointmentCreate
from appointment.service import AppointmentService
from base.base_token import BaseToken
from base.jwt_bearer import JWTBearer
from user.service import UserService


router = APIRouter()
appointment_service = AppointmentService()

@router.get("/appoinments")
def get_appoinments():
    return appointment_service.get_all()

@router.post("/appoinments")
def create_appoinment(payload: AppointmentCreate, token:BaseToken=Depends(JWTBearer())):
    payload.patient_id = token.id
    return appointment_service.create(payload)


@router.get("/appoinments/{id}")
def get_appoinment(id: int):
    return appointment_service.get_by_id(id)

@router.put("/appoinments/{id}")
def update_appoinment(id: int, payload: AppointmentCreate):
    return appointment_service.update(id, payload.to_dict())


@router.delete("/appoinments/{id}")
def delete_appoinment(id: int):
    return appointment_service.delete(id)

@router.get("/appoinments/mine/")
def get_appoinment_by_user(token:BaseToken= Depends(JWTBearer())):
    return appointment_service.get_mine(token.id)