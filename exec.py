import os
import shutil

path = "."
string = ".jpg.repair"

temp_folder_name = "temp"
temp_folder_path = path + os.sep + temp_folder_name
try:
    os.mkdir(temp_folder_name)
    print("Create Done.")
except FileExistsError:
    print("Folder Exists.")

file_path_list = [shutil.move(path + os.sep + file_name, temp_folder_path)
                  for file_name in os.listdir(path) if string in file_name]
[os.rename(file_name, file_name.replace(string, "")) for file_name in file_path_list]
[os.remove(file_name) for file_name in os.listdir(path) if "jpg" in file_name]
file_path_list = [shutil.move(temp_folder_path + os.sep + file_path, path) for file_path in
                  os.listdir(temp_folder_path)]
os.rmdir("./temp")

# [shutil.move(file_path, path) for file_path in file_path_list]
