import hashlib
from pystyle import *

choice = Write.Input("Do you want to enter a 'character' password or an 'hashed' password [c/h]", Colors.green_to_yellow, interval=0.005)

if choice == "c":
    password = Write.Input("Enter The Password: ", Colors.green_to_yellow, interval=0.005)
    password = hashlib.sha256(password.encode()).hexdigest()
    Write.Print(f"Hashed password : {password}", Colors.purple_to_red, interval=0)
else:
    password = Write.Input("Enter The hash: ", Colors.green_to_yellow, interval=0.005)

pass_file = Write.Input(f"\nDrag the password file with all the passwords ('/' in the file path must be remplaced by '\\'): ", Colors.green_to_yellow, interval=0.005) 
x = 0
myfile = open(pass_file, "r")
while myfile:
    line        = myfile.readline()
    hash_object = hashlib.sha256(line.encode())
    hex_dig     = hash_object.hexdigest()
    pass_hex    = hashlib.sha256(password.encode())

    x = x + 1

    if x % 2 == 0:
        Write.Print(f"Checking if: {pass_hex.hexdigest()} = {hex_dig} | Value : {line}", Colors.purple_to_red, interval=0)
    else:    
        Write.Print(f"Checking if: {pass_hex.hexdigest()} = {hex_dig} | Value : {line}", Colors.blue_to_purple, interval=0)
    if hex_dig == pass_hex:
        Write.Print("The pass was found : {line}", Colors.purple_to_red, interval=0)
        break
myfile.close()