from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

mensaje = "clave123"
token = fernet.encrypt(mensaje.encode())
print("Encriptado:", token)

desencriptado = fernet.decrypt(token).decode()
print("Original:", desencriptado)


