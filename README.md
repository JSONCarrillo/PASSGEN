# PASSGEN: FOSS Password Manager

## Table of Contents
1. Description
2. Dependencies
3. Planned Additions

## Description
PASSGEN is a Free and Open Source Password Manager built using Python. 

---

Users open the EXE file found in 'dist' folder and are greeted with a tkinter-based GUI. 

Users can then generate a password and save it to an sqlite database, delete password profiles, as well as edit password attributed usernames and websites.

Passwords are generated in lengths from 8-24 using lower & upper case letters, numbers, and special characters.

## Dependencies
PASSGEN uses ttkbootstrap, tkinter, pillow, and pyinstall. 
CD into PASSGEN directory and run command:

`pip install -r passgen/dependencies.txt`

This should install all neccassary dependencies.


## Planned Additions

1. Give user option to remove numbers and special characters from password generation
