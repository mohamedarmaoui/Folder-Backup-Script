# Folder-Backup-Script
Project Description
This Python script provides an automated solution for backing up a specified folder to a destination directory. The backup creates a timestamped folder to ensure unique backups and tracks the number of files copied. It is designed for simplicity and reliability, making it suitable for personal or small-scale data management tasks.

Features 
Automated Backup: Copies an entire folder recursively to a chosen destination.
Timestamped Backups: Generates unique backup folder names using the current date and time (format: backup_YYYY-MM-DD_HH-MM-SS).
File Count Display: Reports the total number of files backed up after completion.
Error Handling: Checks for the existence of source and destination paths and handles common errors gracefully.
User-Friendly Prompts: Interactive input for source and destination paths.
Setup Instructions
Prerequisites
Python 3.x installed on your system. Download from python.org if needed.
Installation
Download or copy the script code into a file named backup_script.py.
Save the file in a convenient directory.
Technologies Used
Python: Core programming language for the script.
shutil: Standard library module for high-level file operations ( copying directories).
os: Standard library module for interacting with the operating system (path checks and directory creation).
datetime: Standard library module for generating timestamps.
