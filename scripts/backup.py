#!/usr/bin/env python3
import sys
import os
from datetime import datetime
from shutil import copy2, copytree

'''
command in shell: python3 name_current_call_file files_or_dirs_to_backup or command "all"
'''

# Create directory to backups
place_for_backups = "/home/darek/backup"
current_place = os.getcwd()

try:
    os.chdir(f"{place_for_backups}")
except FileNotFoundError:
    print("Directory to make backups are created!")
    os.mkdir(f"{place_for_backups}")
# end


def create_dir_name():
    dir_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    backup_path = f"{place_for_backups}/{dir_name}"
    return backup_path


backup_path = create_dir_name()
os.mkdir(backup_path)
os.chdir(current_place)

for arg in sys.argv[1:]:
        if sys.argv[1] == 'all':
            arg = current_place.split("/")[-1]
            path_to_full_dir = current_place.replace(f"/{arg}", "")
            os.chdir(path_to_full_dir)
            copytree(arg, f"{backup_path}/{arg}")
            break
        elif os.path.isfile(arg):
            copy2(arg, backup_path)
        elif os.path.isdir(arg):
            copytree(arg, f"{backup_path}/{arg}")


