from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column("User_id", Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    nickname = Column("User_name", String(50), nullable=False)
    name = Column("Name", String(50), nullable=False)
    lastName = Column("Last_name", String(50), nullable=False)
    email = Column("Email_add", String(100), nullable=False)
    masters = relationship("Master", back_populates="user")
    passwords = relationship("Pass", back_populates="user")



