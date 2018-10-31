#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests
from bs4 import BeautifulSoup

url = 'http://www.washington.edu/home/peopledir/'

r = requests.post(url, data={'term': 'Information School', 'method': 'dept', 'whichdir': 'staff', 'length': 'full'})

#DEBUG print(r.status_code, r.reason)

soup = BeautifulSoup(r.text, 'html.parser')

names = soup.select("div.contentcell h3")
#for person in names:
 #   print(person.string)

titles = soup.select("div.contentcell ul.multiaddr")
for person in titles:
    jobs = person.descendants
    for position in jobs:
        print(position.string)
    print("\n ---- \n")

#progress note - when descendents was contents, it only showed the last one. swapped to descendants, now it repeats one of them
