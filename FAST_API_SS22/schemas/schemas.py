from pydantic import BaseModel


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    user_id:str
    username: str


class TokenResponse(BaseModel):
    access_token:str
    type_token:str


    