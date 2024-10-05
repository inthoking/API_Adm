from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

# Crear un nuevo usuario
def create_user(db: Session, user: UserCreate):
    db_user = User(nickname=user.User_name, name=user.Name, lastName=user.Last_name, email=user.Email_add)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener usuario por ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
