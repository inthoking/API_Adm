from pydantic import BaseModel

class PassBase(BaseModel):
    Pass: bytes

class PassCreate(PassBase):
    pass

class Pass(PassBase):
    Pass_id: int
    Master_pass_id: int
    User_id: int

    class Config:
        from_attributes = True
