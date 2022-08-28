import requests
import json
import random
from rich import print

# script for uploading file on github gists
# based on: https://gist.github.com/joshisumit/35e9ee3e68e5210af331


def prepare_gist_files(pairs):
    """pairs is list of tuples: (filename, content)"""
    files = {}
    for filename, content in pairs:
        content_dict = {'content': content}
        files[filename] = content_dict
    return files
    
    
def gists_upload(API_TOKEN, description, files, public=False):
    """create github gists upload"""
    url = "https://api.github.com/gists"
    headers = {
        'Authorization': "token {}".format(API_TOKEN),
        "Accept": "application/vnd.github+json",
        }
    params = {'scope':'gist'}
    payload = {
        "description": description,
        "public": public,
        "files": files,
    }
    # ******** upload file ********
    data = json.dumps(payload)
    response = requests.post(url, headers=headers, params=params, data=data)
    return response
    
    
def list_gists(API_TOKEN):
    """list authenticated user gists"""
    headers = {
        'Authorization': "token {}".format(API_TOKEN),
        "Accept": "application/vnd.github+json",
        }
    gists_response = requests.get('https://api.github.com/gists', headers=headers)
    gists = gists_response.json()
    return gists
    
    
if __name__ == "__main__":
    # ******** prepare example content ********
    words = ['colossal', 'sheet', 'fill', 'modern', 'sulky', 'appear', 'dependent', 'argue', 'potato', 'eatable', 'talk', 'coat']
    content = [random.choice(words) for x in range(200)]
    regular_content = ','.join(content)
    reversed_content = ','.join(reversed(content))
    sorted_content = ','.join(sorted(content))
    pairs = [
        ('content.csv', regular_content),
        ('reverse.csv', reversed_content),
        ('sorted.csv', sorted_content),
        ]
    files = prepare_gist_files(pairs)
    
    # ******** upload files ********
    API_TOKEN = 'API_TOKEN'  # create personal access token: https://github.com/settings/tokens
    description = "GIST created by python code"
    response = gists_upload(API_TOKEN, description, files)
    print(response)
    
    # ******** list gists ********
    gists = list_gists(API_TOKEN)
    for gist in gists:
        print(gist)
        