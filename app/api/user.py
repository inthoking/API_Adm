from http import HTTPStatus
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.user import create_user
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    userdto = UserRead.model_validate(db_user)
    userdto_json = userdto.model_dump()
    return JSONResponse(status_code=HTTPStatus.CREATED, content={"message": "creación exitosa", "data": userdto_json})
