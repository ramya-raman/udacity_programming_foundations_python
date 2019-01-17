import string
import os

def rename_files() : 
    file_list = os.listdir(r"G:\Python27\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"G:\Python27\prank")

    for file_name in file_list :
        os.rename( file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
