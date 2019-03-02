import sys
import os
import requests


def script_path():
    '''set current path to script_path'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def simple_read(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
        f.close()
    return data
    
    
def simple_write(file, data):
    '''simple_write data to .txt file, with specified data'''
    with open(file, "w") as f:
        f.write(str(data) + "\n")
        f.close()
    return True
    
    
def get_content(url):
    try:
        res = requests.get(url)
        content = res.text
        status = res.status_code
    except:
        content = ''
        status = 0
    return content, status
    
    
if __name__ == "__main__":
    script_path()
    file = 'urls.txt'
    data = simple_read(file)
    # urls = [item.split('|')[0] for item in data]  # just parse in some way
    urls = ['http://' + url for url in urls]
    responseOk = []
    for key, url in enumerate(urls):
        content, status = get_content(url)
        print("{}. <{}> --> {}".format(key, status, url))
        
        # check if response is positive(set proper filter
        if not status in (0, 404):
            responseOk.append(url)
    simple_write('out.txt', '\n'.join(responseOk))
