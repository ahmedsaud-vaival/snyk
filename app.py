# backup_rotation.py
import os
import shutil
import zipfile
from datetime import datetime

BACKUP_SOURCE = "mydata"
BACKUP_DIR = "backups"
MAX_BACKUPS = 5

os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup():
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = os.path.join(BACKUP_DIR, f"backup_{date_str}.zip")
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for root, _, files in os.walk(BACKUP_SOURCE):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, BACKUP_SOURCE))
    print(f"Backup created: {zip_name}")

def rotate_backups():
    backups = sorted(os.listdir(BACKUP_DIR))
    while len(backups) > MAX_BACKUPS:
        oldest = backups.pop(0)
        os.remove(os.path.join(BACKUP_DIR, oldest))
        print(f"Removed old backup: {oldest}")

if __name__ == "__main__":
    create_backup()
    rotate_backups()
