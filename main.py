
from database.operations import create_user
from database.formats import UserCreate, MasterCreate
from key.encrypt import read_key_iv_pem, encrypt_data, decrypt_data
from fastapi import FastAPI





app = FastAPI()

@app.post("/users/")
async def new_user(user: UserCreate, master: MasterCreate):
    return create_user (user, master)

