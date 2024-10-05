from pydantic import BaseModel

class MasterBase(BaseModel):
    Master_pass: bytes

class MasterCreate(MasterBase):
    pass

class Master(MasterBase):
    Master_pass_id: int
    User_id: int

    class Config:
        orm_mode = True
