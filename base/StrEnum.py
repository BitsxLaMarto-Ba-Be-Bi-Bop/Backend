
from enum import Enum
from sqlalchemy import String, TypeDecorator


class StrEnum(TypeDecorator):
    impl = String
    def __init__(self, enumtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enumtype = enumtype

    @property
    def python_type(self):
        return self._enumtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)
    
    def possible_vals(self):
        return {e.name: e.value for e in self._enumtype}