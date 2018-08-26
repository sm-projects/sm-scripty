import os
import glob

# Enter the directory
from typing import Union

directory = input("Enter the full path name of the directory: ")

os.chdir(directory)

for file in glob.glob("*.csv"):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]  # type: Union[bytes, str]
    new_file_name = file_name[:-2] + extension

    try:
        os.rename(file,new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file,new_file_name))