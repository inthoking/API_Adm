import requests

# Solicitar datos al usuario

#class UserCreate(BaseModel):
# User_name: str
#Name: str
#Last_name: str
#Email_Add= str

#class MasterCreate(BaseModel):
#    Master_pass: bytes



User_name = str(input("Introduce tu nombre de usuario: "))
Name = str(input("Introduce tu nombre: "))
Last_name= str(input("Introduce Apellido: "))
Email_Add= str(input("Ingresa Correo: "))
Master_pass= str(input("Ingresa Contraseña: "))


# Datos del usuario en formato JSON
UserCreate = {
    "User_name": User_name,
    "Name": Name,
    "Last_name": Last_name,
    "Email_Add": Email_Add
}
MasterCreate={
    "Master_pass": Master_pass,
}
data = {
    "user": UserCreate,
    "master": MasterCreate
}



# URL de la API
api_url = "http://127.0.0.1:8000/users/"

# Enviar datos a la API
response = requests.post(api_url, json=data )

# Verificar la respuesta de la API
if response.status_code == 200:
    print("Usuario creado exitosamente")
else:
    print(f"Error al crear el usuario: {response.status_code} - {response.text}")


