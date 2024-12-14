from datetime import UTC, datetime, timedelta
from http import HTTPStatus

from fastapi import HTTPException
from user.model import User, UserType
import jwt

from dateutil import parser

ACCESS_TOKEN_EXPIRE_MINUTES = 3000
SECRET_KEY = 'secret'
ALGORITHM='HS256'
class BaseToken:
    # user_service = UserService()

    id: int = 0
    expt: int = 0
    email: str = ''
    type: str = ''
    # available: bool = True
    # roles: str = ''
    # is_service: bool = False
    # token_type: str = ''
    # is_admin: bool = False

    def __init__(self, user: User):
        # if user is None:
        #     raise Exception('error')
        self.expt = (
            datetime.now(UTC) +
            timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))).isoformat()
        for _ in [_ for _ in dir(self) if _.startswith('__') is False and _.endswith('__') is False]:
            if _ in dir(user):
                setattr(self, _, getattr(user, _))
    def from_token(self, token: str):
        data = BaseToken.decode(token)
        # print(data)
        for _ in [_ for _ in dir(self) if _.startswith('__') is False and _.endswith('__') is False]:
            if  _ in data:
                setattr(self, _, data[_])
        if type(dict['type']) is str:
            self.type = UserType(data['type'])
        return self

    def to_token(self) -> str:
        return BaseToken.encode(self.__dict__)

    # def user_set(self) -> str:
    #     self.user_service.update_token(self)
    #     return self.to_token()

    # def check(self, role: list[Role]) -> bool:
    #     types = [t.value for t in self.role_service.get_all()]
    #     if (self.role not in types) and (not self.is_service):
    #         return False
    #     return True

    # @classmethod
    def decode(token):
        try:
            return jwt.decode(token.encode('utf-8'),
                              SECRET_KEY,
                              algorithms=[ALGORITHM])
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )

    # @classmethod
    def encode(dict):
        if type(dict['type']) is not str:
            dict['type'] = dict['type'].value
        return jwt.encode(dict.items(),
                          SECRET_KEY,
                          algorithm=ALGORITHM)

    def verify(token):
        dict = BaseToken.decode(token)
        user = BaseToken.user_service.get_by_id(dict["id"])
        if user.type != UserType(dict["type"]):
            print(f'{user.type} {dict["type"]}')
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )
        data = BaseToken(None).from_token(token)
        #TODO: comprovar tipus de token

        # if dict['type'] == TokenType.AccessToken.value and user.token != token:
        #     raise Error(ErrorCode.AUTH_INVALID_CREDENTIALS,[])
        # Here your code for verifying the token or whatever you use
        if parser.parse(dict["expt"]) < datetime.now(UTC):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Invalid authentication credentials",)
        return True

    # @classmethod
    # def get_data(token: str):
    #     # return BaseToken(None).from_token(token)
    #     # type = TokenType.ACCESS.value
    #     # if not BaseToken.is_service(token):
    #     type = BaseToken.decode(token).get('token_type')
    #     if type == TokenType.AccessToken.value:
    #         return AccesToken(None).from_token(token)
