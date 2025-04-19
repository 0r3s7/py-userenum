# Python script for local User enumeration (Linux/Windows tested).
# Usage: Place the script into local Users folder (windows) or /home folder (linux) and run it.
# Prerequisites: local admin privileges (windows), sudo (linux), python3 installed on target

import os

# List OS System Name

os_name=os.name

print(f"This is the OS Name: {os_name}\n")

#List Home dir in UNIX systems and walking subdirs

print("Now I'll start enumerating for posix...\n")

if os.name == 'posix':
    path="/home/"
    files=os.listdir(path)
    print(f"Home Folder Content:\n{files}")
    print("\nWalking through Home Dir...\n")
    path_walk='.' #current dir
    for root, dirs, files in os.walk(path_walk): #root=current_dir;dirs=subdirs;files=list_of_files
        print(f"Exploring {root}...\n")
        print(f"Subdirectories {dirs}...\n")
        print(f"Files {files}...\n")
        print('-' *40)

#List Home dir in NT systems and walking subdirs

print("Now I'll start enumerating for NT...\n")

if os.name == 'nt':
    path="C:/Users/"
    files=os.listdir(path)
    print(f"Users Folder Content:\n{files}")
    print("\nWalking through Users Dir...\n")
    path_walk='.' #current dir
    for root, dirs, files in os.walk(path_walk): #root=current_dir;dirs=subdirs;files=list_of_files
        print(f"Exploring {root}...\n")
        print(f"Subdirectories {dirs}...\n")
        print(f"Files {files}...\n")
        print('-' *40)

print("\nEnd Of Program")