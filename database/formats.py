from pydantic import BaseModel

class UserCreate(BaseModel):
    User_name: str
    Name: str
    Last_name: str
    Email_Add: str

class MasterCreate(BaseModel):
    Master_pass: bytes


class PassCreate(BaseModel):
    pass_data: bytes
