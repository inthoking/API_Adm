from sqlalchemy.orm import Session
from app.models.password import Pass
from app.schemas.password import PassCreate

# Crear un nuevo pass
def create_pass(db: Session, pass_obj: PassCreate, user_id: int, master_id: int):
    db_pass = Pass(pass_data=pass_obj.Pass, user_id=user_id, master_id=master_id)
    db.add(db_pass)
    db.commit()
    db.refresh(db_pass)
    return db_pass

# Obtener pass por ID
def get_pass(db: Session, pass_id: int):
    return db.query(Pass).filter(Pass.id == pass_id).first()

# Obtener todos los passes
def get_passes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pass).offset(skip).limit(limit).all()
