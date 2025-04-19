# Python script for local User enumeration (Linux/Windows tested) with *.txt output
# Usage: Place the script into local Users folder (windows) or /home folder (linux) and run it.
# Prerequisites: local admin privileges (windows), sudo (linux), python3 installed on target

import os
from datetime import datetime

# Log file setup
log_filename = "system_enum_log.txt"
log_file = open(log_filename, "w", encoding="utf-8")

def log_print(text):
    print(text)                 # Stampa a video
    log_file.write(text + "\n") # Scrive su file

def log_header(title):
    sep = "=" * 60
    log_print(f"\n{sep}")
    log_print(f"{title}")
    log_print(f"{sep}\n")

def log_section(subtitle):
    log_print(f"\n[+] {subtitle}\n")

# Main
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_header(f"SYSTEM ENUMERATION SCRIPT - {now}")

# OS info
os_name = os.name
log_section("Operating System Info")
log_print(f"os.name: {os_name}")

# Se POSIX (Linux/Mac)
if os_name == 'posix':
    log_section("Listing /home directory (UNIX-like system)")
    try:
        path = "/home/"
        files = os.listdir(path)
        log_print(f"Contents of /home:\n{files}")
    except Exception as e:
        log_print(f"Error listing /home: {e}")

    log_print("\nWalking through current directory ('.'):\n")
    for root, dirs, files in os.walk('.'):
        log_print(f"Exploring {root}...")
        log_print(f"Subdirectories: {dirs}")
        log_print(f"Files: {files}")
        log_print('-' * 40)

# Se NT (Windows)
elif os_name == 'nt':
    log_section("Listing C:/Users directory (Windows NT-like system)")
    try:
        path = "C:/Users/"
        files = os.listdir(path)
        log_print(f"Contents of C:/Users:\n{files}")
    except Exception as e:
        log_print(f"Error listing C:/Users: {e}")

    log_print("\nWalking through current directory ('.'):\n")
    for root, dirs, files in os.walk('.'):
        log_print(f"Exploring {root}...")
        log_print(f"Subdirectories: {dirs}")
        log_print(f"Files: {files}")
        log_print('-' * 40)

log_section("End of Program")
log_file.close()
