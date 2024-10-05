from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column("User_id", Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    nickname = Column("User_name", String, nullable=False)
    name = Column("Name", String, nullable=False)
    lastName = Column("Last_name", String, nullable=False)
    email = Column("Email_add", String, nullable=False)
    master = relationship("Master", back_populates="user")
    password = relationship("Pass", back_populates="user")



