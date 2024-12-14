from fastapi import Depends, FastAPI
from fastapi.routing import APIRoute
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy import create_engine
from base.base_model import BaseModel
from base.base_schema import BaseSchema
from base.base_token import BaseToken
from base.jwt_bearer import JWTBearer
from user.model import User
from user.router import router as user
from appointment.router import router as appointment
from hospital.router import router as hospital

from base.settings import Settings
from fastapi.middleware.cors import CORSMiddleware

from user.service import UserService
from base.ia import *

from user_patient.model import UserPatient
from user_doctor.model import UserDoctor
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=Settings.database_url)
connect_args = {"check_same_thread": False}
engine = create_engine(Settings.database_url, connect_args=connect_args)
BaseModel.metadata.create_all(engine)
app.include_router(user)
app.include_router(appointment)
app.include_router(hospital)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specifies the origins to allow (use ["*"] for all)
    allow_credentials=True,
    allow_methods=["*"], # Specifies the method to allow (GET, POST, DELETE, etc.), use ["*"] for all
    allow_headers=["*"],  # Specifies the headers to allow, use ["*"] for all
)

user_service: UserService = UserService()

class LoginIn(BaseSchema):
    mail: str
    password: str

@app.post("/login", summary="Authenticate User")
def login(credentials: LoginIn):
    user:User = user_service.get_by_mail(credentials.mail)
    if user is None:
        return {"message": "Invalid credentials"}
    if not user_service.get_password_hash(credentials.password) == user.hashed_password:
        return {"message": "Invalid credentials"}
    return {"token": BaseToken(user).to_token()}
    # return auth_service.login(credentials.username, credentials.password)

@app.get("/me", summary="Get current user")
def me(token: BaseToken = Depends(JWTBearer())):
    return token

for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.tags[-1].replace(
            ' ', '').lower() if len(route.tags) > 0 else ''
        route.operation_id += '_' + route.name

