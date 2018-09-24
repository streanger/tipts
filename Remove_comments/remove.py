#script remove comments from cpp, c, and js files
#as parameter put file to be cleared
import os
import sys
import re

def remove_comments(string):
    ''' copied from https://stackoverflow.com/questions/2319019/using-regex-to-remove-comments-from-source-files '''
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)
    
def read_file(path, rmnl=False):
    try:
        with open(path, "r", encoding="utf-8") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
    except MemoryError:
        print(">-- memory error")
        fileContent = []
    except:
        fileContent = []
    return fileContent    
    
    
if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        file = args[0]
    else:
        print("--< no file specified")
        sys.exit()
    try:
        content = "".join(read_file(file))
        noComments = remove_comments(content)
        print(noComments)
    except:
        print("--< can't read ", file)
        