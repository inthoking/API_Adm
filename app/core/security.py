from passlib.context import CryptContext
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Crear un contexto de criptografía con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para verificar contraseñas usando bcrypt
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Función para hashear contraseñas usando bcrypt
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Leer la clave y el IV desde un archivo .PEM
def read_key_iv_pem(filename: str):
    with open(filename, 'rb') as f:
        data = f.read()
        salt = data[:16]
        iv = data[16:32]
        key = data[32:]
    return key, iv, salt

# Función para cifrar datos
def encrypt_data(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    data_padded = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    return encryptor.update(data_padded) + encryptor.finalize()

# Función para descifrar datos
def decrypt_data(data_encrypted: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    datos_padded = decryptor.update(data_encrypted) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(datos_padded) + unpadder.finalize()

# Ejemplo de uso
# key, iv, salt = read_key_iv_pem('secrets/key_iv.pem')
# data = b"Datos secretos que quiero cifrar"
# encrypted_data = encrypt_data(data, key, iv)
# decrypted_data = decrypt_data(encrypted_data, key, iv)
# print(f"Original: {data}")
# print(f"Cifrado: {encrypted_data}")
# print(f"Descifrado: {decrypted_data}")
