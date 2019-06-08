''' script for get files from 'https://doc.lagout.org' '''
import sys
import os

import urllib.request
import urllib.parse

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path
    
    
def make_dir(current_path, new_dir):
    ''' make new dir and return new path '''
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_path = os.path.join(current_path, new_dir)
    return new_path
    
    
def simple_read(file):
    '''simple_read data from specified file'''
    content = []
    with codecs.open(file, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read().splitlines()
    content = [item.replace('/var/www/html/doc', '') for item in content]
    return content
    
    
def get_full_list(file):
    data = []
    with open(file, "r", encoding="utf-8", errors='ignore') as f:
        data = f.read().splitlines()
    data = [item.replace('/var/www/html/doc', '') for item in data]
    data = [(item, item.split('/')[-1]) for item in data]
    return data
    
    
def filter_data(data, filter):
    ''' filter data in format --> (url, file) '''
    out = [(url, file) for (url, file) in data if filter in file]
    return out
    
    
def get_file_from_url(data, dir):
    new_dir = make_dir(script_path(), dir)
    for (url, file) in data:
        local = os.path.join(new_dir, file)
        full_url = urllib.parse.urljoin('https://doc.lagout.org', url)
        print(full_url)
        full_url = full_url.replace(' ', '%20')
        urllib.request.urlretrieve(full_url, local)
    return True
    
    
if __name__ == "__main__":
    script_path()
    data = get_full_list('find.txt')
    
    keywords = ['python', 'network', 'arduino']
    for key in keywords:
        filtered = filter_data(data, key)
        header = '\n' + '\n'.join(['-----' * 10, key.upper().center(len('-----' * 10)), '-----' * 10]) + '\n'
        files = header + '\n'.join([file for url, file in filtered])
        print(files)
        filtered = filtered[:3]
        status = get_file_from_url(filtered, key)
