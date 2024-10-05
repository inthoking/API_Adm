from sqlalchemy import Column, ForeignKey, Integer, LargeBinary
from sqlalchemy.orm import relationship
from app.database import Base

class Master(Base):
    __tablename__ = "master_pass"

    id = Column("Master_pass_id", Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    masterPass = Column("Master_pass", LargeBinary, nullable=False)
    idUser = Column("User_id", Integer, ForeignKey('users.User_id'), nullable=False)
    user = relationship("User", back_populates="masters")
    passwords = relationship("Pass", back_populates="master")