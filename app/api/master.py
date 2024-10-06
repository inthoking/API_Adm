from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.master import create_master, get_masters_for_user
from app.crud.user import get_user
from app.schemas.master import MasterCreate, MasterRead

router = APIRouter()

@router.post("/users/{user_id}/masters/", response_model=MasterRead)
def add_master_to_user(user_id: int, master: MasterCreate, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    masters = get_masters_for_user(db, user_id=user_id)
    if len(masters) >= 3:
        raise HTTPException(status_code=400, detail="User cannot have more than 3 master keys")

    db_master = create_master(db=db, master=master, user_id=user_id)
    masterdto = MasterRead.model_validate(db_master)
    masterdto_json = masterdto.model_dump()
    return JSONResponse(status_code=HTTPStatus.CREATED, content={"message": "creación exitosa", "data": masterdto_json})
