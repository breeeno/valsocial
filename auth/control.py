import datetime
from typing import Optional
import jwt
from decouple import config
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from persons.control import hash_password
from persons.model import Person
from settings import session

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


class AuthController:
    email: str
    password: str

    def __init__(self, email: str = None, password: str = None):
        self.email = email
        self.password = password

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return hash_password.verify(plain_password, hashed_password)

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            email_user = payload.get("sub")
            if email_user is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail="Invalid authentication credentials")
            user = session.query(Person).filter_by(email=email_user).first()
            return user
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    def authenticate_user(self):
        user = session.query(Person).filter_by(email=self.email).first()
        if user is None:
            return False
        if not AuthController.verify_password(self.password, user.password):
            return False
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
