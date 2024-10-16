from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization 
import base64

# Carica la chiave privata
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    
# Carica la chiave pubblica
with open('public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

message = input("Inserisci il messaggio da firmare e verificare: ")

# Firma con la chiave privata
signed = private_key.sign(message.encode(), padding. PKCS1v15 (), hashes. SHA256()) 

# Verifica della firma con la chiave pubblica
try:
    encrypted_b64 = base64.b64encode(signed).decode('utf-8')
    public_key.verify(signed, message.encode(), padding.PKCS1v15(), hashes.SHA256())
    print("\nBase64 della firma:", encrypted_b64)
    print("\nMessaggio originale da confrontare:", message)
    print("\nLa firma è valida.")
except Exception as e:
    print("La firma non è valida.", str(e))