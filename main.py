#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import pandas as pd

# import helper functions
from keywords import gen_wordcloud
from job_desc import get_jd

# initialising 
new_title = []
new_comp = []
new_loc = []
new_time = []
new_link = []
word_list = ['', 'analyst', 'engineer', 'scientist']


# select either data analyst/engineer/scientist
while True:
    choice = input('Please indicate preferred job position: \n 1. Data Analyst \n 2. Data Engineer \n 3. Data Scientist \n')
    if choice not in ['1', '2', '3']:
        print('Invalid choice, please try again.')

    else:
        word = word_list[int(choice)]
        print('You have selected Data ' + word.capitalize())
        break


# number of pages to scrape from
num_page = int(input('Please enter number of pages to scrape from (max 10): '))


# get job title, company name, location, time of post and the respective link
for i in range(1, num_page + 1):

    URL = 'https://www.jobstreet.com.sg/en/job-search/data-jobs-in-singapore/{}'.format(i)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id = 'contentContainer')

    job_elems = results.find_all('article', 
                                 class_ = 'FYwKg _3j_fQ _2mOt7_6 _1A6vC_6 _29sNS _58veS_6')


    for job_elem in job_elems:

        title_elem = job_elem.find('div', 
                                   class_ = 'FYwKg _2j8fZ_6 sIMFL_6 _1JtWu_6', 
                                   string = lambda text: word in text.lower())

        company_elem = job_elem.find('span', 
                                     class_ = 'FYwKg _1GAuD C6ZIU_6 _6ufcS_6 _27Shq_6 _29m7__6')
        
        location_elem = job_elem.find('span', 
                                      class_ = 'FYwKg _1gtjJ _1GAuD _29LNX')
        
        time_elem = job_elem.find('span', 
                                  class_ = 'FYwKg _1GAuD C6ZIU_6 _1_nER_6 u7OQ5_6 _29m7__6')
        
        link_elem = job_elem.find('a')['href']

        # in case a specific job posting does not contain any of these elements
        if None in (title_elem, company_elem, location_elem, time_elem, link_elem):
            continue


        new_title.append(title_elem.text.strip())
        new_comp.append(company_elem.text.strip())
        new_loc.append(location_elem.text.strip())
        new_time.append(time_elem.text.strip())
        new_link.append('https://www.jobstreet.com.sg' + link_elem)


# create a pandas dataframe with all the information
job_list = pd.DataFrame({
'Job_Title' : new_title,
'Company' : new_comp,
'Location' : new_loc,
'First_Posted' : new_time,
'Link' : new_link
    })


# get the job description from eeach job posting
get_jd(job_list, 'Link')


# generate a wordcloud for each job description
gen_wordcloud(job_list, 'Job_Desc', word)


# save dataframe to a csv file
job_list.to_csv('data_' + word + '_jobs.csv')