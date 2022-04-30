__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
from zipfile import ZipFile


def clean_cache():
    path = 'c:/Users/marco/Winc/files/cache'  # I would like to generalize the string path using os.getcwd(),but in order to do it i need to run VS directly from the dir \files, in that case I cant use wimpcy check.
    if os.path.isdir(path) is False:
        os.mkdir(path)
    else:
        files = os.listdir(path)
        for x in files:
            os.remove(f'{path}/{x}')
    return None


def cache_zip(file_path, dir_path):
    clean_cache()
    my_zip = ZipFile(file_path)
    my_zip.extractall(dir_path)
    return None


def cached_files():
    my_list = []
    for x in os.listdir('C:\\Users\\marco\\Winc\\files\\cache'):
        if os.path.isfile(f'C:\\Users\\marco\\Winc\\files\\cache\\{x}'):
            my_list += [f'C:\\Users\\marco\\Winc\\files\\cache\\{x}']
    return my_list


def find_password(my_list=cached_files()):
    psw = ''
    for my_file in my_list:
        f = open(my_file)
        for x in f:
            if 'password' in x:
                psw = x[x.find(' ')+1:-1]
        f.close()
    return psw
