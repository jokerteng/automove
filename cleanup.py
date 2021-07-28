import os

path = "."
sub_path = "./temp"
[os.remove(file_name) for file_name in os.listdir(path) if "jpg" in file_name]
[os.remove(sub_path + os.sep + file_name) for file_name in os.listdir(sub_path)]
