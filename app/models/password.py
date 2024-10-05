from sqlalchemy import Column, ForeignKey, Integer, LargeBinary
from sqlalchemy.orm import relationship
from app.database import Base

class Pass(Base):
    __tablename__ = "pass"

    id = Column("Pass_id", Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    passData = Column("Pass", LargeBinary, nullable=False)
    idMaster = Column("Master_pass_id", Integer, ForeignKey('master_pass.Master_pass_id'), nullable=False)
    idUser = Column("User_id", Integer, ForeignKey('users.User_id'), nullable=False)
    user = relationship("User", back_populates="passwords")
    master = relationship("Master", back_populates="passwords")
