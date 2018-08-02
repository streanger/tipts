#script to create new dir, and check if exists
import os
import sys

def make_dir(new_dir):
    'make new dir, switch to it and retur new path'
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_path = os.path.join(path, new_dir)
    return new_path

path = make_dir('Test')
print(path)
