from fastapi import FastAPI
from app.api import user, master, password
from key.encrypt import read_key_iv_pem, encrypt_data, decrypt_data
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(master.router, tags=["masters"])
app.include_router(password.router, tags=["passes"])