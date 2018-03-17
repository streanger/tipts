import re

def find_emails(CONTENT=[]):
    reForm = re.compile(r'[\w\.-]+@[\w\.-]+')
    #CONTENT = "test some@dot.email.com and this free@gmail.com like grres@zbz.com"
    try:
        return reForm.findall(CONTENT)
    except:
        return []
