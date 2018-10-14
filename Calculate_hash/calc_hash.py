import os
import sys
import hashlib

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def calc_hash(file):
    '''
    copied from https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
    TL;DR use buffers to not use tons of memory.
    '''
    
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return md5.hexdigest(), sha1.hexdigest()
    
    
if __name__ == "__main__":
    path = script_path()
    args = sys.argv[1:]
    if args:
        file = args[0]
    else:
        print("no file specified...")
        sys.exit()

    md5Hash, sha1Hash = calc_hash(file)
    print("File: {}\nMD5: {}\nSHA1: {}".format(file, md5Hash, sha1Hash))