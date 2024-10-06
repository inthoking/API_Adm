from sqlalchemy.orm import Session
from app.models.master import Master
from app.schemas.master import MasterCreate

# Crear un nuevo master
def create_master(db: Session, master: MasterCreate, user_id: int):
    db_master = Master(master_pass=master.Master_pass, user_id=user_id) #genera un registro
    db.add(db_master)
    db.commit()
    db.refresh(db_master)
    return db_master

# Obtener master por ID
def get_master(db: Session, master_id: int):
    return db.query(Master).filter(Master.id == master_id).first()

# Obtener todos los masters capaz no se usa por si acaso
def get_masters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Master).offset(skip).limit(limit).all()

# Obtener claves maestras para un usuario específico 
def get_masters_for_user(db: Session, user_id: int):
    return db.query(Master).filter(Master.user_id == user_id).all()