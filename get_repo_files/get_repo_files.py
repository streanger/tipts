'''
    script for count lines of code in github repos
    no support for files tree
    extended and simple mode
    when creating package use following functions:
        main                    --simple main function (return general info)
        main_extended           --return dails about files
        get_all_git_repos       --to get all repos, based on username
        repo_files              --to get files based on repos list
        
    06.08.2019 --> script is ready, to create package from it
        
    dd.mm.yyyy --> some info
        subinfo
        subinfo
        
'''

import sys
import os
import urllib.request
import bs4 as bs
import requests
import urllib.parse
import time


def script_path():
    currentPath = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(currentPath)
    return currentPath
    
    
def simple_write(file, data):
    '''simple_write data to .txt file, with specified data'''
    with open(file, "w") as f:
        f.write(str(data))
        f.close()
    return True
    
    
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
    
    
def get_file_from_url(url):
    '''read file from specified url, to memory'''
    content = urllib.request.urlopen(url).read()
    out = content.decode('utf-8')
    return out
    
    
def get_all_git_repos(username, full=False):
    '''returns list of repos based on specified username'''
    base = 'https://github.com/'
    if False:
        url = base + username + '?tab=repositories'
    else:
        # url = urllib.parse.urljoin('https://github.com/', username, '?tab=repositories')  # won't work, as i expected - no time for now, to check it
        url = urllib.parse.urljoin('https://github.com/', username)
        url = urllib.parse.urljoin(url, '?tab=repositories')
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
    '''list all files from repo; do it recursively'''
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
        
        
def repo_files(repos, toFilter):
    base = 'https://github.com'
    rawBase = 'https://raw.githubusercontent.com'
    data = {}
    strOut = ''
    for key, repo in enumerate(repos):
        full = list_recursive(repo, repo, True)
        out = flatten(full)
        out = list(set(out))       # remove dupli (for now dk why duplicates appears)
        if toFilter:
            out = [item for item in out if item.endswith(toFilter)]
            
        out = [item.replace(base, rawBase).replace('/blob', '', 1) for item in out]     # change to raw
        data['{:02d}. {} '.format(key, repo)] = out     # store files from single repo under one key
        strOut += '{:02d}. {} '.format(key, repo) + '\n'
        strOut += '\n'.join(['\t' + item for item in out]) + '\n'*2
    return data, strOut
    
    
def count_lines(links, blank):
    number = 0
    linksNumber = len(links)
    strOut = ''
    for key, link in enumerate(links):
        file = get_file_from_url(link)
        if blank:
            # cut every lines, even empty
            lines = len(file.splitlines())
            number += lines
        else:
            # count only lines with code
            lines = len([item for item in file.splitlines() if item.strip()])
            number += lines
        strOut += '{:04d}/{:04d}. total_lines: {}, current_lines: {}, current_file: {}\n'.format(key, linksNumber, number, lines, link)
    return number, strOut
    
    
def main_extended(username, toFilter=None, blank=True, timer=True):
    ''' 
        count lines of github repository, with specified username, files extenions(toFilter),
        with or without blank lines(blank parameter)
        timer is optional
        creates directory with username name and puts there following files:
        repo_files.txt, links.txt, total.txt, total_log.txt
        its extended version of main function
    '''
    if timer:
        print('script starts, please wait...')
        begin = time.time()
        
    if not os.path.exists(username):
        os.makedirs(username)
    currentPath = os.path.realpath(os.path.dirname(sys.argv[0]))
    dirPath = os.path.join(currentPath, username)
    
    
    repos = get_all_git_repos(username, True)
    if not toFilter:
        toFilter = ()
    data, strOut = repo_files(repos, toFilter)
    simple_write(os.path.join(dirPath, 'repo_files.txt'), strOut)
    
    links = [x for y in list(data.values()) for x in y]
    simple_write(os.path.join(dirPath, 'links.txt'), '\n'.join(links))
    
    totalNumberOfLines, log = count_lines(links, blank)
    out = 'username: {}\ntotalFiles: {}\ntotalNumberOfLines: {}\nfilteredBy: {}\nwithBlankLines: {}'.format(username,
                                                                                                            len(links),
                                                                                                            totalNumberOfLines,
                                                                                                            toFilter,
                                                                                                            blank)

    simple_write(os.path.join(dirPath, 'total.txt'), out)
    simple_write(os.path.join(dirPath, 'total_log.txt'), log)
    
    if timer:
        finish = time.time()
        print('script execution finished in: {}[s]\nYou can open newly created files'.format(round(finish - begin, 4)))
    return out
    
    
def main(username, toFilter=None, blank=True, timer=True):
    if timer:
        print('script starts, please wait...')
        begin = time.time()
        
    repos = get_all_git_repos(username, True)
    if not toFilter:
        toFilter = ()
    data, strOut = repo_files(repos, toFilter)
    links = [x for y in list(data.values()) for x in y]
    totalNumberOfLines, log = count_lines(links, blank)
    out = 'username: {}\ntotalFiles: {}\ntotalNumberOfLines: {}\nfilteredBy: {}\nwithBlankLines: {}'.format(username,
                                                                                                            len(links),
                                                                                                            totalNumberOfLines,
                                                                                                            toFilter,
                                                                                                            blank)
    if timer:
        finish = time.time()
        print('script execution finished in: {}[s]'.format(round(finish - begin, 4)))
    return out
    
    
if __name__ == "__main__":
    script_path()
    username = 'streanger'
    
    # simple main
    out = main(username, ('.py', ), False, True)
    print(out)
    
    input('\npress enter, to run main_extended...\n')
    
    # extended main
    out = main_extended(username, ('.py', ), False, True)
    print(out)
    
    
'''
info:
    -searching only for public repos
    -need to do it recursively
    -for now it list files
    -finally it need to count lines of (filtered) files
    -think of add some timer
    -make some module of that
    -
    
'''
