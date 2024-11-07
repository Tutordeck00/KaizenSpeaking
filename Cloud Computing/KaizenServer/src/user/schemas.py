from pydantic import BaseModel, ConfigDict
from uuid import  UUID

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str
    nickname: str = None
    phone_number: str = None
    role: str = "user"

class UserLogin(BaseModel):
    username: str
    password: str

class UserDetailResponse(BaseModel):
    id: UUID
    username: str
    full_name: str
    nickname: str = None
    phone_number: str = None

    class Config:
        model_config = ConfigDict(
            from_attributes=True,
            json_encoders={UUID: str}
        )

class UserResponse(BaseModel):
    id: UUID
    username: str
    full_name: str
    nickname: str = None
    phone_number: str = None

    class Config:
        model_config = ConfigDict(
            from_attributes=True,
            json_encoders={UUID: str}
        )
