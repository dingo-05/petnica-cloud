import json

file_name = (r'D:\!PETNICA\Projekat\http\petnica-cloud\connect\users.json')
#lokacija fajla
with open(file_name,'r+') as json_file:
        data = json.load(json_file)
#dodavanje korisnika
def create_user(username, password):
    with open(file_name,'r+') as json_file:
        data = json.load(json_file)
        new_user = {
            "username": username,
            "password": password
        }
        print(password)
        data["users"].append(new_user)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)

#def verify_username(username):
#    with open(file_name,'r+') as json_file:
#        data = json.load(json_file)
#        for user in data['users']:
#            if username == user['username']: 
#                print("User found successfully. ")
#                return 1
#            else:
#                print("User not found. ")
#                return 2

def verify_username(username):
    provera = 0
    for user in data["users"]:
        if user['username'] == username:
            print("User found successfully. ")
            provera = 1
            break
        else:
             provera = 2
    return provera
        
def verify_password(password):
    provera = 0
    for user in data["users"]:
        if user['password'] == password: 
            print("Password is correct. ")
            provera = 1
            break
        else:
            provera = 2
    return provera
            
            #provera podataka
#def verify_data(username, password):
#    with open(file_name,'r+') as json_file:
#        data = json.load(json_file)
#        for key, value in data.items():
#            if key == username: 
#                if value == password:
#                    print(f"Welcome {username}")
#                    return 1
#                else: 
#                    print(f"Invalid password")
#                    return 2
#            else: 
#                print(f"Do you want to crate new account? 1 - YES / 2 - NO")
#                ans = input()
#                if ans == "1":
#                    print(f"Input password: ")
#                    password = input()
#                    new_user = {
#                        "username": username,
#                        "password": password
#                    }
#                    data["users"].append(new_user)
#                    json_file.seek(0)
#                    json.dump(data, json_file)
#                else: 
#                    break
