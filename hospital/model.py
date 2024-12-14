from sqlalchemy import Column, Integer, String
from base.base_model import BaseModel


class Hospital(BaseModel):
    __tablename__ = "hospital"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    address: str = Column(String(255), nullable=False)
    phone: str = Column(String(20), nullable=False)