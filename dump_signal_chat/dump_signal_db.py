# -*- coding: utf-8 -*-
import sys
import os
import json
import shutil
from rich import print

"""
useful:
    https://www.yoranbrondsema.com/post/the-guide-to-extracting-statistics-from-your-signal-conversations/
    https://stackoverflow.com/questions/13654122/how-to-make-python-get-the-username-in-windows-and-then-implement-it-in-a-script
    https://rado0z.github.io/Decrypt_Android_Database
    https://github.com/sqlcipher/sqlcipher
    https://www.youtube.com/watch?v=SFHGeetZ0po
    <path>\\DB_Browser_SQLite\DB Browser for SQLCipher.exe"
    https://www.johndball.com/pulling-encrypted-signal-messages-off-of-desktop-os-for-forensics/
"""

def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_json(filename):
    """read json file to dict"""
    data = {}
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return data
    
    
def copy_signal_db():
    """copy signal db file to current location"""
    username = os.getlogin()
    original_db_path = r'C:\Users\{}\AppData\Roaming\Signal\sql\db.sqlite'
    original_db_path = original_db_path.format(username)
    db_path = shutil.copy(original_db_path, '.')
    return db_path
    
    
def read_signal_key():
    """for windows"""
    username = os.getlogin()
    key_path = r'C:\Users\{}\AppData\Roaming\Signal\config.json'
    key_path = key_path.format(username)
    data = read_json(key_path)
    signal_key = data['key']
    return signal_key
    
    
if __name__ == "__main__":
    script_path()
    db_path = copy_signal_db()
    db_path = r'.\db.sqlite'
    signal_key = read_signal_key()
    print(db_path, signal_key)
    