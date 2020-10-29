#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def get_jd(df, col):

	"""
	Get the job description for each job posting.

	Input: Dataframe to reference from, column to iterate.
	Output: a list of job description.
	"""
   
	jd = []

	for links in df[col]:
		r = requests.get(links)
		soup = BeautifulSoup(r.text,'html.parser')

		for tag in soup.find_all('div', class_ = 'vDEj0_6'):
			jd.append(tag.text.strip())

	jd = jd[0::2]

	df['Job_Desc'] = jd