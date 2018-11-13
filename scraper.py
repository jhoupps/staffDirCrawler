#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests
from bs4 import BeautifulSoup
import csv

with open('position_data.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name','Department Searched', 'Position', 'At'])

    #Part 1 - getting the UW department Names

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
            clean_name = name.string.replace("'", "")
            clean_name = clean_name.replace("&apos;", "")
            clean_name = clean_name.replace(", MD", "")
            clean_name = clean_name.replace(",", "")
            row_contents = [clean_name, department]
            jobs = titles.descendants
            sketchy_work_around = ""
            for job in jobs:
                if str(job.string) != "None":
                    if str(job.string) != sketchy_work_around:
                        #print(job.string)
                        row_contents.append(job.string)
                        sketchy_work_around = str(job.string)
            filewriter.writerow(row_contents)
                        
    #Part 3 - actually searching the directory

    for department_name in output:
        searchDir(department_name)


