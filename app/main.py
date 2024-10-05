from fastapi import FastAPI
from app.api import user, master, password
from app.database import Base, engine
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(master.router, tags=["masters"])
app.include_router(password.router, tags=["passes"])