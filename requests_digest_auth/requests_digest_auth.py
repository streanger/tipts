import hashlib
import requests
from rich import print
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

"""
useful:
    https://stackoverflow.com/questions/23254013/http-digest-basic-auth-with-python-requests-module
    https://stackoverflow.com/questions/20658572/python-requests-print-entire-http-request-raw
    https://httpbin.org/#/Auth
    https://betterprogramming.pub/accessing-the-web-in-python-using-requests-5fe5bb2bd822
    https://en.wikipedia.org/wiki/Digest_access_authentication
    https://stackoverflow.com/questions/2384230/what-is-digest-authentication
    https://www.youtube.com/watch?v=vRvMLWDR6Uw
    https://riptutorial.com/python/example/30786/authentication
    
download large file:
    response = request.get(url_to_download_large_file, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)
"""

def md5_sum(content):
    """calc md5 sum of content
    
    content is type of bytes
    keywords: md5, hash
    """
    md5_hash = hashlib.md5(content).hexdigest()
    return md5_hash
    
    
if __name__ == "__main__":
    url = 'https://httpbin.org/digest-auth/auth/user/password'
    response = requests.get(url, auth=HTTPDigestAuth('user', 'password'))
    # HA1 as example; not needed
    HA1 = md5_sum('user:realm:password'.encode('utf-8'))
    print('HA1: {}'.format(HA1))
    print('status_code: {}'.format(response.status_code))
    print(response.text)
    print(response.cookies)
    print(response.headers)
    print('\nhistory: {}'.format(response.history))
    print('\nfirst request: {}'.format(response.history[0].headers))
