import shutil
import os
from datetime import datetime

def count_files_in_folder(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def backup_folder(source_folder, destination_dir):
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder_name = f"backup_{timestamp}"
    backup_path = os.path.join(destination_dir, backup_folder_name)
    
    num_files = count_files_in_folder(source_folder)
    
    try:
        shutil.copytree(source_folder, backup_path)
        print(f"Backup completed successfully to: {backup_path}")
        print(f"Number of files copied: {num_files}")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    source = input("Enter the path to the folder you want to back up: ").strip()
    destination = input("Enter the path to the destination directory: ").strip()
    
    backup_folder(source, destination)