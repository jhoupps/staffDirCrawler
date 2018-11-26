#A web crawler for traversing the UW staff directory, located at http://www.washington.edu/home/peopledir/ 

#A project by J. Houppermans, for an Informatics 300 Group Project

import requests
from bs4 import BeautifulSoup
import csv

with open('position_data.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    #colnames uses magic number for max amount of titles on a person observed
    colnames = ["Name", "Department_Searched"]
    for i in range(1, 9):
        colnames.append("Position_"+str(i))
        colnames.append("At_"+str(i))

    filewriter.writerow(colnames)

    #Part 1 - getting the UW department Names

    url = 'http://www.washington.edu/about/academics/departments/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    dep_names = soup.select("div.uw-body-copy li a")

    output = []
    for dep_name in dep_names:
        output.append(str(dep_name.string))
    output = output[1:] #removes "home" from the department list
    #Part two - method that sends requests to the staff directory 

    url2 = 'http://www.washington.edu/home/peopledir/'


    def searchDir(department):
        r2 = requests.post(url2, data={'term': department, 'method': 'dept', 'whichdir': 'staff', 'length': 'full'})
        
        soup = BeautifulSoup(r2.text, 'html.parser')

        names = soup.select("div.contentcell h3")
        #titles = soup.select("div.contentcell ul.multiaddr")
        titles_listing = soup.select("ul.dir-listing")

        ##debug - complete rewrite that next section, snag algorithms from it as needed
        #documentation note - titles_html_block is a bs4 tag

        for name, titles_html_block in zip(names, titles_listing):
            clean_name = name.string.replace("'", "")
            clean_name = clean_name.replace("&apos;", "")
            clean_name = clean_name.replace(", MD", "")
            clean_name = clean_name.replace(",", "")

            clean_department = department.replace(", ", " ̦")
            
            #debug progress - this prints every single name, and doesn't skip anyone
            multi = titles_html_block.select("ul.multiaddr")
            solo = titles_html_block.select("ul.title")

            #len = 1 or len =0 depending on which it is. Does grab both

            both_kinds_list = []
            #people with the multiaddr tag typically (though not always)
            #   have more than one title
            #and have the format <li> content <br> </li>
            #   except for the last element, which is <li> content </li>   
            if(len(multi) > 0):
                both_kinds_list = multi[0].select("li")
                
            #people with the solo tag typically (though not always)
            #   have just one title
            # and the format is <li> content </li>  
            elif(len(solo) > 0):
                both_kinds_list = solo[0].select("li")

            row_contents = [clean_name, clean_department]

            if(len(both_kinds_list) > 0):
                for title in both_kinds_list:
                    clean_title = title.get_text().replace(", Emeritus", "- Emeritus")
                    job_and_department = clean_title.split(",")
                                    
                    ##might not actually be necessary, with the emeritus change
                    clean_job = job_and_department[0].replace(",", " ̦")
                    clean_job_department = job_and_department[1].replace(",", " ̦")

                    row_contents.append(clean_job.strip())
                    row_contents.append(clean_job_department.strip())
                    
                    filewriter.writerow(row_contents)

    #Part 3 - actually searching the directory

#FLAG - DEBUG - DEACTIVATED MULTI-DEPARTMENT FUNCTIONALITY
    for department_name in output:
        searchDir(department_name)

