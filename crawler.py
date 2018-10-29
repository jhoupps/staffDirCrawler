#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests

url = 'http://www.washington.edu/home/peopledir/'

r = requests.post(url, data={'term': 'Information School', 'method': 'dept', 'whichdir': 'staff', 'length': 'full'})

print(r.status_code, r.reason)

print("Web Content: \n \n ~~~~~~~~ \n \n")

print(r.text)
