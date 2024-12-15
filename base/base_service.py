import importlib

from fastapi import HTTPException
from fastapi_sqlalchemy import db

# from src.error import *
from base.base_model import ModelBase
from base.base_schema import BaseSchema


class BaseService:
    name = 'base_service'
    __model__: ModelBase = None

    @classmethod
    def get_password_hash(cls, password):
        return password

    @classmethod
    def get_all(cls):
        return db.session.query(cls.__model__).all()
    
    @classmethod
    def get_by_id(cls, id):
        obj = db.session.query(cls.__model__).filter(cls.__model__.id == id).first()
        if obj is None:
            raise HTTPException(status_code=404, detail=f'{cls.name} with id={id} not found')
            # raise Exception(f'{cls.name} with id={id} not found')
        return obj
    @classmethod
    def create(cls, data: BaseSchema):
        instance = cls.__model__(**data.model_dump())
        db.session.add(instance)
        db.session.commit()
        return instance
    
    @classmethod
    def update(cls, id, kwargs):
        instance = cls.get_by_id(id)
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.session.commit()
        db.session.refresh(instance)
        return instance
    
    @classmethod
    def delete(cls, id):
        instance = cls.get_by_id(id)
        db.session.delete(instance)
        db.session.commit()
        return instance
    
    # @classmethod
    # def add_labbel(cls, id, labell:dict[str, str]):

    def needs_service(service):

        def wrapper(f):

            def get_service(*args):
                s = args[0]
                ser = service
                if type(service) is str:
                    # equiv. of your `import matplotlib.text as text`
                    ser = importlib.import_module(
                        'src.' + service.replace('Service', '').lower() +
                        '.service')
                    ser = getattr(ser, service)

                if getattr(s, ser.name) is None:
                    setattr(s, ser.name, ser())
                return f(*args)

            return get_service

        return wrapper