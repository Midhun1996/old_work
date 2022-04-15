import os
import shutil
import datetime

source_folder = r'C:\Users\WELCOME\Desktop\thread module'

destination_folder = r'C:\Users\WELCOME\Desktop\demo_copy'

for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)