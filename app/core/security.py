import bcrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


# Función para verificar contraseñas usando bcrypt
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Función para hashear o encriptar como se quieras decir contraseñas usando bcrypt
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()  # Genera un nuevo salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hashea la contraseña
    return hashed.decode('utf-8')

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

#TEGNO QEU AGREGAR EL ENCRIPTADO ASIMETRICO 
# Ejemplo de uso
# key, iv, salt = read_key_iv_pem('secrets/key_iv.pem')
# data = b"Datos secretos que quiero cifrar"
# encrypted_data = encrypt_data(data, key, iv)
# decrypted_data = decrypt_data(encrypted_data, key, iv)
# print(f"Original: {data}")
# print(f"Cifrado: {encrypted_data}")
# print(f"Descifrado: {decrypted_data}")
