''' this is clear script
    only files are listed
    no tree
'''
import urllib.request
import bs4 as bs
import requests
import urllib.parse
# from urllib.parse import urlparse
import sys


def get_content(url=''):
    res = requests.get(url)
    content = res.text
    status = res.status_code
    return content, status
    
    
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
    
    
def filter_files(data, filter):
    out = []
    return out
    
    
def get_file_from_url(url):
    content = urllib.request.urlopen(url).read()
    out = content.decode('utf-8')
    return out
    
    
def url_destination(url):
    return urllib.parse.urlparse(url).netloc
    
    
def get_all_git_repos(username, full=False):
    ''' my own --> https://github.com/streanger '''
    base = 'https://github.com/'
    url = base + username + '?tab=repositories'
    # url = urllib.parse.urljoin('https://github.com/', username, '?tab=repositories')  # won't work, as i expected - no time for now, to check it
    content, status = get_content(url)
    soup = bs.BeautifulSoup(content, 'lxml')
    href_tags = soup.find_all(href=True)
    out = [item['href'] for item in href_tags]
    #filter
    filtered = [item for item in out if (item.startswith('/' + username + '/')) and (item.count('/') == 2)]
    if full:
        return [urllib.parse.urljoin(base, item) for item in filtered]
    else:
        return filtered
        
        
def list_recursive(repo, current, first):
    ''' list all files from repo 
        do it recursively
    '''
    base = 'https://github.com/'        # for now it need to cotain this stuff
    begin = repo.replace(base, '', 1)   # only first item
    content, status = get_content(repo)
    soup = bs.BeautifulSoup(content, 'lxml')
    href_tags = soup.find_all(href=True)
    out = [item['href'] for item in href_tags]
    # filter by tree and blob
    if first:
        treeBegin = '/' + begin + '/' + 'tree'
        blobBegin = '/' + begin + '/' + 'blob'
    else:
        treeBegin = '/' + begin + '/'
        blobBegin = '/' + begin + '/'
        blobBegin = blobBegin.replace('tree', 'blob', 1)   # for now
        
    tree = [urllib.parse.urljoin(base, item) for item in out if item.startswith(treeBegin)]
    blob = [urllib.parse.urljoin(base, item) for item in out if item.startswith(blobBegin)]
    all = tree + blob
    
    if tree:
        if first:
            return [list_recursive(item, repo, False) for item in tree[1:]] + blob
        else:
            return [list_recursive(item, repo, False) for item in tree[:]] + blob
    else:
        return all
        
        
if __name__ == "__main__":
    username = 'streanger'
    repos = get_all_git_repos(username, True)
    repos = [repos[4], repos[11], repos[18]]
    
    toFilter = ('.py', '.c', '.cpp' , '.txt')
    toFilter = ()
    for key, repo in enumerate(repos):
        # input('{:02d}. start with repo: {} '.format(key, repo))
        print('{:02d}. {} '.format(key, repo))
        full = list_recursive(repo, repo, True)
        out = flatten(full)
        if toFilter:
            out = [item for item in out if item.endswith(toFilter)]
        strOut = '\n'.join(['\t' + item for item in out])
        print(strOut)
        print()
        
        
'''
info:
    -searching only for public repos
    -need to do it recursively
    -for now it list files
    -finally it need to count lines of (filtered) files
    -
    
'''
