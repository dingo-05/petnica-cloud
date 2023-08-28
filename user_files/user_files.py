import os
import subprocess

def create_user_folder(username):
    folder_path = fr'C:\Mladen\Piton\parent\{username}'
    
    # Create user's folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder created for user '{username}'")

def set_folder_permissions(username):
    folder_path = fr'C:\Mladen\Piton\parent\{username}'
    
    # Set permissions using icacls command
    subprocess.run(['icacls', folder_path, '/inheritance:r'])
    
    # Grant user permission to their folder
    subprocess.run(['icacls', folder_path, f'/grant:r', f'{username}:(OI)(CI)F'])
    
    # Deny user access to parent folder
    subprocess.run(['icacls', folder_path, f'/deny', f'{username}:(OI)(CI)RX'])
    
    print(f"Permissions set for user '{username}'")

if __name__ == "__main__":
    username = input("Enter the username: ")
    
    create_user_folder(username)
    set_folder_permissions(username)
