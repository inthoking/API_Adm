from pydantic import BaseModel

class MasterBase(BaseModel):
    Master_pass: str

class MasterCreate(MasterBase):
    pass

class MasterRead(MasterBase):
    Master_pass_id: int
    User_id: int

    class Config:
        from_attributes = True


#funciones del DTO
