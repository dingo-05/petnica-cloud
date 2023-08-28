import os
import subprocess
import shutil

    server_path = fr'C:\Mladen\Piton\Users\{username}'

def send_files(username):
    folder_path = input("Unesi lokaciju fajla koji zelis da uploadujes")
    shutil.copy(folder_path, server_path)

def create_user_folder(username):
    
    # Create user's folder if it doesn't exist
    if not os.path.exists(server_path):
        os.mkdir(server_path)
        print(f"Folder created for user '{username}'")

def set_folder_permissions(username):
    server_path = fr'C:\Mladen\Piton\Users\{username}'
    
    # Set permissions using icacls command
    subprocess.run(['icacls', server_path, '/inheritance:r'])
    
    # Grant user permission to their folder
    subprocess.run(['icacls', server_path, f'/grant:r', f'{username}:(OI)(CI)F'])
    
    # Deny user access to parent folder
    subprocess.run(['icacls', server_path, f'/deny', f'{username}:(OI)(CI)RX'])
    
    print(f"Permissions set for user '{username}'")

    subprocess.run(['explorer',server_path])

if __name__ == "__main__":
    username = input("Enter the username: ")
    
    create_user_folder(username)
    set_folder_permissions(username)
    send_files(username)

