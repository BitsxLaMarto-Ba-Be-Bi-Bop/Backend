from fastapi import Depends, FastAPI
from fastapi.routing import APIRoute
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy import create_engine
from user.router import router as user
from base.settings import Settings

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=Settings.database_url)

app.include_router(user)

# admin_app.add_de

for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.tags[-1].replace(
            ' ', '').lower() if len(route.tags) > 0 else ''
        route.operation_id += '_' + route.name

