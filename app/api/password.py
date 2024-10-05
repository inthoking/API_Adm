from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.password import create_pass
from app.crud.user import get_user
from app.schemas.password import PassCreate, Pass

router = APIRouter()

@router.post("/users/{user_id}/masters/{master_id}/passes/", response_model=Pass)
def add_pass_to_master(user_id: int, master_id: int, pass_obj: PassCreate, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_pass = create_pass(db=db, pass_obj=pass_obj, user_id=user_id, master_id=master_id)
    return db_pass
