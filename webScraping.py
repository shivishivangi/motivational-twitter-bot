# webScraping.py

# extract randomized motivational quotes from different websites

import requests
from bs4 import BeautifulSoup
from random import randrange


URL = 'https://sharpquotes.com/positive-quotes/' 
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

def getQuote(): 
    # results = soup.find(id='content')

    quote_elem = soup.find('article', class_ = 'post-69 post type-post status-publish format-standard hentry category-quotes tag-be-positive tag-be-positive-quotes tag-george-bernard-shaw-quote tag-helen-keller-quote tag-mahatma-gandhi-quote tag-paulo-coelho-quote tag-positive-quotes tag-positive-thinking-quotes tag-positivity-quote tag-winston-churchill-quote tag-zig-ziglar-quote')
    # results = soup.find(id='post-69')
    quotes = quote_elem.find_all('p')
    random = randrange(3, 102)

    print("hi")
    count = 0

    for quote in quotes:
        count += 1
        qtext = quote.text
        if (count == random):
            tweet = qtext
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

    print("Final Tweet: " + tweet)

getQuote()
