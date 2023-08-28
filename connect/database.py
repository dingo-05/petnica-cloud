import json
import os

file_name = (r'D:\BOBAN\Desktop\Danilo\Petnica\rac1l\Projekat\petnica-cloud\connect\users.json')
#citanje fajla


#dodavanje korisnika
def create_user(username, password):
    with open(file_name,'r+') as json_file:
        data = json.load(json_file)
        new_user = {
            "username": username,
            "password": password
        }
        data["users"].append(new_user)
        json_file.seek(0)
        json.dump(data, json_file)

#provera podataka
def verify_data(username, password):
    with open(file_name,'r+') as json_file:
        data = json.load(json_file)
        for user in data['users']:
            if user['username'] == username: 
                if user['password'] == password:
                    print(f"Welcome {username}")
                    break
                else: 
                    print(f"Invalid password")
            else: 
                print(f"Do you want to crate new account? 1 - YES / 2 - NO")
                ans = input()
                if ans == "1":
                    print(f"Input password: ")
                    password = input()
                    new_user = {
                        "username": username,
                        "password": password
                    }
                    data["users"].append(new_user)
                    json_file.seek(0)
                    json.dump(data, json_file)
                else: 
                    break