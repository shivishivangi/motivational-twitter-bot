# webScraping.py

# extract randomized motivational quotes from 1500 motivational quotes (sharpquotes.com)

import requests
from bs4 import BeautifulSoup
from random import randrange

URL = 'https://sharpquotes.com/motivational-quotes-times-of-crisis/' 
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

def getQuote(): 
    quote_elem = soup.find('article', class_ = 'post-501 post type-post status-publish format-standard hentry category-quotes tag-being-strong-quotes tag-calm-quotes tag-change-quotes tag-character-quotes tag-courage-quotes tag-encouraging-quotes tag-family-quotes tag-friendship-quotes tag-health-quotes tag-hope-quotes tag-humanity-quotes tag-meditation-quotes tag-perseverance-quotes tag-positive-quotes tag-stoic-quotes')
    quotes = quote_elem.find_all('p')
    random = randrange(2, 1501)
    # random = 1501

    # print("hi")
    count = 0

    for quote in quotes:
        qtext = quote.text
        if (count == random):
            tweet = qtext
        count += 1
        # print(qtext)
    
    # get rid of number in the beginning of the quote
    array = tweet.split(".")
    for part in array:
        if (part != array[0]):
            if (part == array[1]):
                newTweet = part
            else:
                newTweet = newTweet + "." + part
            tweet = newTweet.strip()

    # print("Final Tweet: " + tweet)
    return tweet

getQuote()

