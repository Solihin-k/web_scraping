# Web Scraper for Job Search
Web scrape data related jobs from [JobStreet](https://www.jobstreet.com.sg/), one of the go-to job portals in Singapore.

<img src="https://i.ytimg.com/vi/l2Sp3MYoccw/maxresdefault.jpg" width="600" height="300"/>

# Description
Job hunting is one of the most tedious and exhausting things to do. It involves more than searching for open positions and sending your resume to employers. You also need to make sure you’re a good fit for the job, can catch the hiring manager’s attention and are well-prepared to answer interview questions.

<img src="https://cdn01.vulcanpost.com/wp-uploads/2017/01/job-platforms-FI.png" width="600" height="300"/>

The web scraper will help shorten the time taken to search for open positions and also identify some keywords via a wordcloud based on the job description. Hopefully this can help you by freeing up some time to focus on your resume and subsequent follow-ups. <br>
The main URL is set to search for data related jobs in Singapore, but can easily be customised for any positions at any locations.

# Installation

You would need the following packages.
```
pip install requests
pip install bs4
pip install wordcloud
```

Clone the repo and run main.py:
```
git clone https://github.com/Solihin-k/web_scraping.git
```

# Usage

You will be promted for 2 inputs:
1. To specify on the role to look for (Data Analyst, Data Engineer or Data Scientist)
2. Number of pages to scrape from (max is set at 10)

## Output
- a CSV file with the list of job postings
- a wordcloud image based on the job description

Job_Title | Company | Location | First_Posted
------------ | ------------- | ------------ | -------------
Data Analyst | D L Resources Pte Ltd | Singapore | 1d ago

![sample](/Images/analyst_11.png)

For the above position, the wordcloud recognizes keywords such as transformation, visualization and automating. <br>
The maximum number of words for the wordcloud is set to 50, but this too can be easily customised to suit your preference.

# Acknowledgements

Thanks to the team at Real Python for their [tutorial](https://realpython.com/beautiful-soup-web-scraper-python/).
