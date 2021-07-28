import os
import shutil

path = "."
string = ".jpg.repair"

file_list = [file_name for file_name in os.listdir(path) if string in file_name]
file_list = file_list + ["Thumbs.db"]
for file_name in os.listdir(path):
    file_path = path + os.sep + file_name
    if os.path.isfile(file_path):
        if file_name not in file_list:
            os.remove(file_path)
[os.rename(file_name, file_name.replace(string, "")) for file_name in
        [path + os.sep + file_name for file_name in file_list]]
print("Done.")
