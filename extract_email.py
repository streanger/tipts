import re
import html.parser as h
import requests
from sys import argv

def page_content(url=""):
    try:
        return requests.get(url).text
    except:
        print("\n--< wrong url address\n")
        return ""

def find_emails(rC=[]):
    reForm = re.compile(r'[\w\.-]+@[\w\.-]+')
    try:
        emails = reForm.findall(rC)   #rC - replaced content
        return list(set(emails))
    except:
        return []

def find_html_sign(htmlStr=""):
    if not htmlStr:
        return [] #htmlStr = "some &#64; and &#123;"
    reForm = re.compile(r'&#\d+;')  #my 1st useful regex
    thing = reForm.findall(htmlStr)
    return list(set(thing)) #we dont really need duplicates

def html_to_ascii(htmlStr=""):
    if not htmlStr:
        return "" #htmlStr = '&#64;' #just an example
    return h.unescape(htmlStr)

def convert_page(C=""):
    if not C:
        return ""
    signs = find_html_sign(C)
    for item in signs:
        C = C.replace(item, html_to_ascii(item))
    #this is the most fragile part
    for item in ["'", " ", "+"]:
        C= C.replace(item, "")
    return C

def main(argv):
    url = ""
    if len(argv)>0 and type(argv) is list:
        url = argv[0]
    elif type(argv) is str:
        url = argv
    C = page_content(url)   #get full content
    if not C:
        return []
    rC = convert_page(C)    #convert to ascii and replace some stuff
    emails = find_emails(rC)    #extract emails
    return emails


if __name__ == "__main__":
    emails = main(argv[1:])
    print(emails)
