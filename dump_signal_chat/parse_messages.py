# -*- coding: utf-8 -*-
import sys
import os
import json
import datetime
import pandas as pd
from rich import print

"""
useful:
    https://stackoverflow.com/questions/31303728/pandas-cannot-filter-based-on-string-equality
    https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
    https://stackoverflow.com/questions/9758450/pandas-convert-dataframe-to-array-of-tuples
"""


def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def unix_to_datetime(unix_time):
    """convert unix to datetime"""
    out = datetime.datetime.fromtimestamp(unix_time)
    return out
    
    
def write_json(filename, data):
    """write to json file"""
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True
    
    
if __name__ == "__main__":
    script_path()
    filename = 'messages.csv'
    df = pd.read_csv(filename, index_col=0)
    
    # filter db by conversation ID; my notes
    my_conversation_id = "XXXXXXXXXXXXXXXXXXXXXXXX"
    df = df[df['conversationId'].str.strip() == my_conversation_id]
    
    # remove nan values
    df = df[df['body'].notna()]
    
    # iterate over messages
    new_order = ['body', 'sent_at']
    df = df[new_order]
    messages = list(df.itertuples(index=False))
    messages = [(body, str(unix_to_datetime(sent_at/1000))) for index, (body, sent_at) in enumerate(messages)]
    write_json('private_messages.json', messages)
    for index, (body, sent_at) in enumerate(messages):
        print('{})'.format(index+1))
        print(sent_at, body)
        print()
        