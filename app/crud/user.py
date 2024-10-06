from http import HTTPStatus
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.master import Master
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserRead
from app.utils.exceptions import CustomException

# Crear un nuevo usuario
def create_user(db: Session, user: UserCreate):
    try:
        db_user = User(nickname=user.User_name, name=user.Name, lastName=user.Last_name, email=user.Email_add)
        db.add(db_user)
        db.flush()
        db.refresh(db_user)
        hashid = hash_password(user.password)
        db_master = Master(masterPass=hashid, idUser=db_user.id)
        db.add(db_master)
        db.flush()
        db.refresh(db_master)
        db_user = UserRead(User_id=db_user.id, User_name=db_user.nickname, Name= db_user.name, Last_name=db_user.lastName, Email_add=db_user.email)
        db.commit()
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise CustomException(status_code=HTTPStatus.BAD_REQUEST, detail="Datos no válidos" + str(e))
    except Exception as e:
        db.rollback()
        raise CustomException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Error en el servidor" + str(e))

# Obtener usuario por ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
