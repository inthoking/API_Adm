import mariadb
from .database import get_db_connection
from .formats import UserCreate, MasterCreate

#Esta funcion inserta datos dentro de la tabla users, en el campo usuario, tiene que recibir datos de formato UserCreate
def create_user(user: UserCreate, master: MasterCreate):
    conn = get_db_connection() 
    cursor = conn.cursor()
    try:
        # Insertar un nuevo usuario
        cursor.execute(
            "INSERT INTO users (User_name, Name, Last_name, Email_Add) VALUES (?, ?, ?, ?)",
            (user.User_name, user.Name, user.Last_name, user.Email_Add)
        )
        conn.commit()
        
        # Consultar el ID del usuario recién insertado
        cursor.execute(
            "SELECT User_id FROM users WHERE User_name = ?",
            (user.User_name,)
        )
        user_id = cursor.fetchone()

        # Insertar datos en la tabla masterpass usando el ID del usuario
        cursor.execute(
            "INSERT INTO masterpass (Master_pass, User_id) VALUES (?, ?)",
            (master.Master_pass, user_id)
        )
        conn.commit()
    except mariadb.Error as e:
        print(f"Error: {e}") 
        return None
    finally:
        cursor.close()
        conn.close()

        
if __name__== "__main__":
    a="AQUI NO HAY NADA AUN"
    create_user(a)
    

