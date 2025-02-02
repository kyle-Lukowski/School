import hashlib
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
file_path = 'Database.txt'


def login(dict):
    username = input("Input Username: ")
    password = input("Input Password: ")
    password = calculate_md5_hash(password) #hash password

    if dict.get(username) == password:
        print("Successful login") #will fail if username doesent exist or if value of password isnt the input
    else:
        userinput = input("Failed login, try again (1) or menu (2)")
        if userinput == 1:
             login(dict)
        else:
             menu(dict)
        


def register(dict):
    username = input("Input Username: (Must be at least 6 chars)")
    password = input("Input Password: (Must be at least 6 chars)")
    password = calculate_md5_hash(password)
    
    if username in dict:
         userinput = input("username already taken choose retry (1) or menu (2)")
         if userinput == 1:
              register(dict)
         else:
              menu(dict)
    else:
         dict[username] = password
         print(dict)
         print("Successfully registered")
         menu(dict)


def calculate_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

def menu(my_dict):
    choice = 0
    while choice != '3':
        choice = input("Register (1): \n login (2) \n Exit (3)")

        if choice == '1':
            register(my_dict)
        elif choice == '2':
            login(my_dict)
        else:
             break

def exitprogram(my_dict, key):
    with open(file_path, 'w') as file: #encrypt and close file
                for username, value in my_dict.items():

                    encryptedusername = encrypt(username, key)
                    encryptedvalue = encrypt(value, key)

                    file.write(encryptedusername.decode("utf-8", "ignore"))
                    file.write("\t")
                    file.write(encryptedvalue.decode("utf-8", "ignore"))
                    file.write(f"\n")
                file.close()

def encrypt(data, key):
        data = pad(data.encode(),16)
        cipher = AES.new(key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(data))

def decrypt(data, key):
        data = base64.b64decode(data)
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(data),16)
                           

def Main():
    print("Inputting the wrong key will make logging in impossible as the password file will be encrypted still")
    hexkey = input("Input the AES key to encrypt/decrypt in hexadecimal format:")
    key = bytes.fromhex(hexkey)
    

    with open(file_path, 'r') as file:
        dict = {}

        for line in file:
            username, value = line.strip().split('\t')

            username = decrypt(username, key) #decrypt then store file into dict
            value = decrypt(value, key)
            username = username.decode('utf-8', "ignore")
            value = value.decode('utf-8', "ignore")

            dict[username] = value

    file.close()
    menu(dict)
    exitprogram(dict, key)
                              

     

    
    

Main()