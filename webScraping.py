# webScraping.py

# take randomized motivational quotes from website

import requests
from bs4 import BeautifulSoup

URL = 'https://www.goodreads.com/quotes/tag/motivation'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find(id='ResultsContainer')
def getQuote(): 
    leftContainer = soup.find('div', class_='leftContainer')

    quoteMediumText_elems = leftContainer.find_all('div', class_='quote mediumText')

    for quote in quoteMediumText_elems:
        text_elem = quote.find('div', {'class':'quoteText'})
        # neededval = text_elem['#text']
        author_elem = quote.find('span', class_='authorOrTitle')
        # location_elem = job_elem.find('div', class_='location')
        if None in (text_elem, author_elem):
            continue
        # print(text_elem.text.strip())

        # print(author_elem.text)
        # print(location_elem.text.strip())
        tweet = text_elem.text.strip()
        print((tweet))
        # print()
    
    return tweet

getQuote()

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
# results = soup.find(id='ResultsContainer')
#
# job_elems = results.find_all('section', class_='card-content')
#
#
# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()
