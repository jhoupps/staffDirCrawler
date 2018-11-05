#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests
from bs4 import BeautifulSoup


#Part one - getting the UW department Names

url = 'http://www.washington.edu/about/academics/departments/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
dep_names = soup.select("div.uw-body-copy li a")

output = []
for dep_name in dep_names:
    output.append(str(dep_name.string))

#Part two - method that sends requests to the staff directory 

url2 = 'http://www.washington.edu/home/peopledir/'


def searchDir(department):

    r2 = requests.post(url2, data={'term': department, 'method': 'dept', 'whichdir': 'staff', 'length': 'full'})
    
    soup = BeautifulSoup(r2.text, 'html.parser')

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
                    
#Part 3 - actually searching the directory

for department_name in output:
    searchDir(department_name)


