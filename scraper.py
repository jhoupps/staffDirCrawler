#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests
from bs4 import BeautifulSoup

url = 'http://www.washington.edu/home/peopledir/'

r = requests.post(url, data={'term': 'Information School', 'method': 'dept', 'whichdir': 'staff', 'length': 'full'})

soup = BeautifulSoup(r.text, 'html.parser')

names = soup.select("div.contentcell h3")
titles = soup.select("div.contentcell ul.multiaddr")

for name, titles in zip(names, titles):
    print(name.string)
    jobs = titles.descendants
    sketchy_work_around = ""
    for job in jobs:
        if str(job.string) != "None":
            if str(job.string) != sketchy_work_around:
                print(job.string)
                sketchy_work_around = str(job.string)
