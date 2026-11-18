from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Key:", key)

f = Fernet(key)
# try:
#     user =  int(input("Enter card number here: ")) 

token = f.encrypt(b"smile")
print("Encrypted:", token)

message = f.decrypt(token)
print("Decrypted:", message)
# except ValueError:
#     print("Just ")



# from cryptography.fernet import Fernet



