from pydantic import BaseModel

class UserBase(BaseModel):
    User_name: str
    Name: str
    Last_name: str
    Email_add: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    User_id: int

    class Config:
        orm_mode = True