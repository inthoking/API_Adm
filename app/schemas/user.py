from pydantic import BaseModel

class UserBase(BaseModel):
    User_name: str
    Name: str
    Last_name: str
    Email_add: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    User_id: int

    class Config:
        from_attributes = True