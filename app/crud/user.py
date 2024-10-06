from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserRead

# Crear un nuevo usuario
def create_user(db: Session, user: UserCreate):
    print("Entró acá")
    db_user = User(nickname=user.User_name, name=user.Name, lastName=user.Last_name, email=user.Email_add)
    print("usuario creado")
    db.add(db_user)
    print("usuario añadido")
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener usuario por ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
