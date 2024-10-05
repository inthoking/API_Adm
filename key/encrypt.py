from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
from cryptography.hazmat.backends import default_backend

# Leer la clave y el IV desde un archivo .PEM que genere anteriormente, por seguridad quizas cambiarlo una vez al mes
def read_key_iv_pem(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        salt = data[:16]
        iv = data[16:32]
        key = data[32:]
    return key, iv, salt

# Función para cifrar datos
def encrypt_data(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    data_padded = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    return encryptor.update(data_padded) + encryptor.finalize()

# Función para descifrar datos
def decrypt_data(data_encryped, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    datos_padded = decryptor.update(data_encryped) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(datos_padded) + unpadder.finalize()

#/Ejemplo
#key, iv, salt = read_key_iv_pem('key_iv_aes.pem')
#texto = b"Este es un texto secreto"
#texto_cifrado = cifrar_datos(texto, key, iv)
#texto_descifrado = descifrar_datos(texto_cifrado, key, iv)
#
#print(f"Texto original: {texto}")
#print(f"Texto cifrado: {texto_cifrado}")
#print(f"Texto descifrado: {texto_descifrado}")
