import sys
import os
import zipfile
import py7zr
from pathlib import Path
# from rich import inspect  # DEBUG


def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def extract_zip_to_bytes(path, password=None):
    """extract zip archive to bytes objects"""
    with zipfile.ZipFile(path, 'r') as zip_ref:
        # inspect(zip_ref, methods=True)
        namelist = zip_ref.namelist()
        objects = [(name, zip_ref.read(name, pwd=password)) for name in namelist]
    return objects
    
    
def extract_zip_to_directory(path, directory, password=None):
    """extract zip archive to directory"""
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(directory, pwd=password)
    return None
    
    
def extract_7z_to_bytes(path, password=None):
    """extract 7z archive to bytes objects"""
    with py7zr.SevenZipFile(path, mode='r', password=password) as z:
        # inspect(z, methods=True)
        objects = [(name, item.read()) for name, item in z.readall().items()]
    return objects
    
    
def extract_7z_to_directory(path, directory, password=None):
    """extract 7z archive to directory"""
    with py7zr.SevenZipFile(path, mode='r', password=password) as z:
        # password_protected = z.password_protected
        # needs_password = z.needs_password()
        # names = z.getnames()
        z.extractall(directory)
    return None
    
    
if __name__ == "__main__":
    script_path()
    directory = Path('unpacked')
    directory.mkdir(exist_ok=True)
    
    if False:
        # ********* zip example *********
        password = b'password'
        filename = 'archive.zip'                # zip with no encryption
        filename = 'archive_password.zip'       # zip with encryption
        path = Path('archives').joinpath(filename)
        objects = extract_zip_to_bytes(path, password=password)
        extract_zip_to_directory(path, directory, password=password)
        print(objects)
        
    if True:
        # ********* 7z example *********
        password = 'password'
        filename = 'archive.7z'                 # 7z with no encryption
        filename = 'archive_password.7z'        # 7z with encryption
        filename = 'archive_encrypted_names.7z' # 7z with names encryption
        path = Path('archives').joinpath(filename)
        objects = extract_7z_to_bytes(path, password=password)
        extract_7z_to_directory(path, directory, password=password)
        print(objects)
        
"""
useful:
    https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/
    ZipFile.extractall(path=None, members=None, pwd=None)
    https://pypi.org/project/py7zr/
    -zipfile package accepts passwords as bytes
    -py7zr package accepts passwords as strings
    
"""
