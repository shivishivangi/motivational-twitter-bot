# quotesFile.py

# takes a motivational quote database and picks a random quote to tweet

import pandas as pd
import xlrd
from random import randrange

def getDataCSV():

    # returns a random quote from quotes.csv

    datafile = pd.read_csv("quotes.csv")
    QUOTE_COL = 1
    AUTHOR_COL = 0

    quoteRow = randrange(0, 1663)
    # print(quoteRow)

    quote = datafile.iloc[quoteRow, QUOTE_COL]
    author = datafile.iloc[quoteRow, AUTHOR_COL]

    tweet = quote + " - " + author
    # print(tweet)

    return tweet


def getMemeData():

    # returns a random quote from MotivationalQuotesDatabase.xlsx (doesn't actually have inspiring quotes...)

    QUOTE_COL = 0 
    AUTHOR_COL = 1
    CATEGORY_COL = 2

    datafile = ("MotivationalQuotesDatabase.xlsx") 
    excelWkbk = xlrd.open_workbook(datafile)
    sheet = excelWkbk.sheet_by_index(0)

    quoteRow = randrange(4, 45578)
    # print(quoteRow)
    # print(sheet.cell_value(quoteRow, QUOTE_COL))

    quote = sheet.cell_value(quoteRow, QUOTE_COL)
    author = sheet.cell_value(quoteRow, AUTHOR_COL)
    category = sheet.cell_value(quoteRow, CATEGORY_COL)
    
    tweet = quote + " - " + author

    # print(tweet)

    tweet = hashtag(tweet, category)

    # print(tweet)

    return tweet
    

def hashtag(tweetStr, category):

    # adds category hashtag to tweet if it does not exceed 280 characters 

    newTweet = tweetStr + " #" + category
    size = len(newTweet)
    addSize = 280 + len(category)

    if (size <= addSize and size > 280):
        return tweetStr
    else: 
        return newTweet


#Run python quotesFile.py to test 

# getDataCSV()
# getMemeData()


