import requests
from bs4 import BeautifulSoup
from csv import writer
import re

#Removing all the tags to earn strings by regular expressions
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

#Using GET 
page = requests.get("https://sites.google.com/view/davidchoi/home/members")

#To crawl specific HTML tag, I used BeutifulSoup module
soup = BeautifulSoup(page.content, "html.parser")

#name storage
name_arr = []
#job_role storage
job_role_arr = []
#....
start_year_arr = []
end_year_arr = []
research_interest_arr = []
current_job_role_arr = []
profile_pic_url_arr = []

#To apply different logic tag by tag, I used cnt variable.
cnt = 0
#Finding all <p></p> tags which have dir='ltr'
people_infos = soup.find_all('p',dir="ltr")
#Iterating the tags
for people in people_infos:
    if people:
        #Removing tags
        txt = cleanhtml(str(people))
        txt.strip()
        #If txt exists
        if txt:   
            #When cnt is even, name, role and year strings are assigned in txt
            if cnt % 2 == 0:
                #Split name and role_year by '('
                name, role_year = txt.split('(')
                name = name.rstrip()
                #Assingn in name storage
                name_arr.append(name)
                role_year = role_year.lstrip()
                #We don't need ')'
                role_year = role_year.replace(')','')
                #Split job_role and year by ','
                job_role, year = role_year.split(',')
                #Assign in job_role storage
                job_role_arr.append(job_role)
                year = year.strip()
                #if '-' is in year, it means end_year is different with start year or end_year ins't finished yet.
                if '-' in year:
                    #If year ends with '-' then end_year isn't finished yet.
                    if year.endswith('-'):
                        start_year = year.replace('-','')
                        end_year = "NA"
                    #Else there exist both start_year and end_year
                    else :
                        start_year, end_year = year.split("-")
                #If there isn't '-', it means start_year and end_year is same.
                else:
                    start_year = year
                    end_year = year
                #Assign them to storage
                start_year_arr.append(start_year)
                end_year_arr.append(end_year)
            else :
                #If txt starts with 'Research', it means current member
                if txt.startswith('Research'):
                    #So current_job_role is "NA"
                    current_job_role = "NA"
                    #If txt ends with ":", no interests
                    if txt.endswith(':'):
                        research_interest = "NA"
                    #Else there is interests
                    else:
                        _,research_interest = txt.split(":")
                        research_interest = research_interest.strip()
                #If txt doesn't start with 'Research', it means alumni.
                else:
                    research_interest = "NA"
                    current_job_role,_ = txt.split('@')
                #Assign them to storage
                research_interest_arr.append(research_interest)
                current_job_role_arr.append(current_job_role)
            #cnt + 1
            cnt += 1
    
#For image URL, same as above code
images = soup.find_all('img',class_="CENy8b")
for image in images:
    profile_pic_url_arr.append(image.get('src'))

#Writing 'problem2_csv.csv' file
f = open("problem2_csv.csv", "w")

#Making it delimited by ',' and '\n'
for i in range(len(name_arr)):
    f.write(name_arr[i] + ',' + job_role_arr[i] + ',' + start_year_arr[i] + ',' + end_year_arr[i] \
        + ',' + research_interest_arr[i] + ',' + current_job_role_arr[i] + ',' + profile_pic_url_arr[i] + '\n')

f.close()
