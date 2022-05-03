__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
from zipfile import ZipFile
path = f'{os.getcwd()}\\cache'
print(os.getcwd())
def clean_cache():
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
    for x in os.listdir(path):
        if os.path.isfile(f'{path}\\{x}'):
            my_list += [f'{path}\\{x}']
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
