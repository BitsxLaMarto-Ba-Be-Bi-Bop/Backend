from fastapi import APIRouter, HTTPException
from hospital.schema import HospitalCreate, HospitalGet
from hospital.service import HospitalService
from typing import List
from pydantic import BaseModel


router = APIRouter()
hospital_service = HospitalService()

@router.get("/hospitals", response_model=List[HospitalGet])
def get_hospitals():
    return hospital_service.get_all()

@router.get("/hospitals/{hospital_id}", response_model=HospitalGet)
def get_hospital(hospital_id: int):
    hospital = hospital_service.get_by_id(hospital_id)
    if hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@router.post("/hospitals", response_model=HospitalGet)
def create_hospital(hospital: HospitalCreate):
    return hospital_service.create(hospital)

@router.put("/hospitals/{hospital_id}", response_model=HospitalGet)
def update_hospital(hospital_id: int, hospital: HospitalCreate):
    updated_hospital = hospital_service.update(hospital_id, hospital)
    if updated_hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return updated_hospital

@router.delete("/hospitals/{hospital_id}", response_model=HospitalGet)
def delete_hospital(hospital_id: int):
    deleted_hospital = hospital_service.delete(hospital_id)
    if deleted_hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return {"message": "Hospital deleted successfully"}

@router.get("/hospitals/generate/")
def generate_hospitals():
    hospitals = hospital_service.create_all()
    return {"message": f"{len(hospitals)} hospitals generated successfully", "hospitals": hospitals}