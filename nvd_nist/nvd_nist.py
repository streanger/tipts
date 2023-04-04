import datetime
import requests
from rich import print

"""
docs: https://nvd.nist.gov/developers/vulnerabilities

"""

url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
end_date = datetime.datetime.now().isoformat(timespec='milliseconds') + '+00:00'
begin_date = (datetime.datetime.now() - datetime.timedelta(10)).isoformat(timespec='milliseconds') + '+00:00'
# params = {'lastModStartDate': begin_date, 'lastModEndDate':end_date}
params = {'pubStartDate': begin_date, 'pubEndDate':end_date}
print(params)
response = requests.get(url, params=params)
vulns = response.json()['vulnerabilities']
