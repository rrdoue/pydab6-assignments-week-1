#! /usr/bin/env python3

# Collab 3 Breakout Exercise: System Ids and User Names


# 1. Use a list comprehension to produce a list of two-element tuples
#   the user id (field index 0) and user name (field index 2) using the
#   `linux-etc-password.txt` file in the zip file.
# 2. Note: You'll have to worry about blank lines and commented lines.
# 3. If you do that, then also try to do it with a dictionary comprehension.

# source file:

# jupyter notebook finished product (list comprehension)
# [
#     (one_line.split(':')[2], one_line.split(':')[0] )
#     for one_line in open('/etc/passwd')
#     if not one_line.startswith('#')
#     if one_line.strip()
# ]

# With some easy python wrapper stuff for the command line

import os

file_and_full_path_name = '/etc/passwd'

print(f"First let's ask for the location of Reuven's /etc/passwd file (full path).\n"
      f"If you don't provide a filename, we will use your system's \n\tunix/linux/macos "
      f"password file.")
user_file = input('Downloaded collab 3 "linux-etc-password.txt" file location: ')

if user_file:
    file_and_full_path_name = user_file

if os.path.exists(file_and_full_path_name):
    print(f'File exists: {file_and_full_path_name}')
else:
    print(f'File does not exist: {file_and_full_path_name}')
    exit()
