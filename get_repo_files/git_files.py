'''script for count lines of code in github repos; cleaned up'''

import sys
import os
import urllib.request
import bs4 as bs
import requests
import urllib.parse
import time


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
        url = urllib.parse.urljoin('https://github.com/', username)
        url = urllib.parse.urljoin(url, '?tab=repositories')
    content, status = get_content(url)
    soup = bs.BeautifulSoup(content, 'lxml')
    href_tags = soup.find_all(href=True)
    out = [item['href'] for item in href_tags]
    
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
    reposNumber = len(repos)
    reposNumberLen = len(str(reposNumber))
    print('search repos progress:')
    for key, repo in enumerate(repos):
        
        # ************ progress line ************
        value = ((key+1)/reposNumber)*100
        line = fill_line(value) + ' {}% [{}/{}]'.format(
            round(value),
            str(key+1).zfill(reposNumberLen),
            reposNumber,
            )
        print('{}'.format(line), end='\r', flush=True)
        
        
        full = list_recursive(repo, repo, True)
        out = flatten(full)
        out = list(set(out))                                                            # remove dupli (for now dk why duplicates appears)
        if toFilter:
            out = [item for item in out if item.endswith(toFilter)]
            
        out = [item.replace(base, rawBase).replace('/blob', '', 1) for item in out]     # change to raw
        data['{}. {} '.format(str(key+1).zfill(reposNumberLen), repo)] = out            # store files from single repo under one key
        strOut += '{}. {} '.format(str(key+1).zfill(reposNumberLen), repo) + '\n'
        strOut += '\n'.join(['\t' + item for item in out]) + '\n'*2
    print('\n')
    return data, strOut
    
    
def fill_line(value):
    '''value -> int from 0-100'''
    number = 25
    line = '-'*number
    point = round((value*number)//100)
    out = line.replace('-', '>', point)
    return out
    
    
def count_lines(links, blank):
    number = 0
    linksNumber = len(links)
    linksNumberLen = len(str(linksNumber))
    strOut = ''
    print('read links progress:')
    for key, link in enumerate(links):
    
        # ************ progress line ************
        value = ((key+1)/linksNumber)*100
        line = fill_line(value) + ' {}% [{}/{}]'.format(
            round(value),
            str(key+1).zfill(linksNumberLen),
            linksNumber,
            )
        print('{}'.format(line), end='\r', flush=True)
        
        
        file = get_file_from_url(link)
        if blank:
            lines = len(file.splitlines())                                      # cut every lines, even empty
            number += lines
        else:
            lines = len([item for item in file.splitlines() if item.strip()])   # count only lines with code
            number += lines
        strOut += '{}/{}. total_lines: {}, lines: {}, link: {}\n'.format(
            str(key+1).zfill(linksNumberLen),
            linksNumber,
            number,
            lines,
            link
            )
    print('\n')
    return number, strOut
    
    
def main(username, toFilter=None, blank=True):
    '''
        -count lines of github repository, with specified:
            username - github account name
            toFilter - files extenions to be searched
            blank - counting blank lines parameter
            
        -creates directory with username name and puts there following files:
            repo_files.txt
            links.txt
            total.txt
            total_log.txt
    '''
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
    
    distance = 19
    out = '{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}'.format(
        'username'.ljust(distance, '.'),
        username,
        'totalFiles'.ljust(distance, '.'),
        len(links),
        'totalNumberOfLines'.ljust(distance, '.'),
        totalNumberOfLines,
        'filteredBy'.ljust(distance, '.'),
        toFilter,
        'countBlankLines'.ljust(distance, '.'),
        blank
        )
        
    simple_write(os.path.join(dirPath, 'total.txt'), out)
    simple_write(os.path.join(dirPath, 'total_log.txt'), log)
    
    finish = time.time()
    print('{}: {} [s]'.format(
        'total time'.ljust(distance, '.'),
        round(finish - begin, 2))
        )
    return out
    
    
if __name__ == "__main__":
    os.chdir(os.path.realpath(os.path.dirname(sys.argv[0])))
    out = main('streanger', ('.py', ), True)
    print(out)
