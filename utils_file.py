import os
from os.path import join

def get_dir_file_names(parent_path, files):    
    return [f'{join(parent_path, file_name)}' for file_name in files]


def get_file_names(dir_name):
    file_names = []    
    for dir_name, dirs, files in os.walk(dir_name):
        file_names += get_dir_file_names(dir_name, files)

    return file_names
    