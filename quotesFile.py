# quotesFile.py

#takes a motivational quote database and picks a random quote to tweet

#limitations:
#  needs to be less than 280 characters
#  if the tweet allows space, needs to include the hashtag with the category

#NOTE: try to figure out if you can make a thread 
# Import pandas
import pandas as pd
from random import randrange

QUOTE_COL = 1
AUTHOR_COL = 0

def parseData():
    # Load csv
    datafile = pd.read_csv("example.csv")
    
    # To open Workbook
    excelWkbk = xlrd.open_workbook(datafile)
    sheet = excelWkbk.sheet_by_index(0)
    
    # For row 0 and column 0
    quoteRow = randrange(0, 1665)
    print(quoteRow)
    print(sheet.cell_value(quoteRow, QUOTE_COL))

    # generate random value for the row 
    # quotes in the excel database start at row value 4 and end at 45578
    # print(randrange(4, 45578))

    quote = sheet.cell_value(quoteRow, QUOTE_COL)
    author = sheet.cell_value(quoteRow, AUTHOR_COL)
    
    tweet = quote + " - " + author

    print(tweet)

    hashtag(tweet)


def hashtag(tweetStr):
    newTweet = tweetStr + " #Motivating"
    # if (tweetStr + " #" + )
    print(newTweet)


parseData()


# PREVIOUS DATAFILE WORK:

# import xlrd

# QUOTE_COL = 0 
# AUTHOR_COL = 1
# CATEGORY_COL = 2

# def parseData():
#     # Give the location of the file
#     datafile = ("MotivationalQuotesDatabase.xlsx")
    
#     # To open Workbook
#     excelWkbk = xlrd.open_workbook(datafile)
#     sheet = excelWkbk.sheet_by_index(0)
    
#     # For row 0 and column 0
#     quoteRow = randrange(4, 45578)
#     print(quoteRow)
#     print(sheet.cell_value(quoteRow, QUOTE_COL))

#     # generate random value for the row 
#     # quotes in the excel database start at row value 4 and end at 45578
#     # print(randrange(4, 45578))

#     quote = sheet.cell_value(quoteRow, QUOTE_COL)
#     author = sheet.cell_value(quoteRow, AUTHOR_COL)
#     category = sheet.cell_value(quoteRow, CATEGORY_COL)
    
#     tweet = quote + " - " + author

#     print(tweet)

#     hashtag(tweet, category, quoteRow)


# def hashtag(tweetStr, tag, row):
#     newTweet = tweetStr + " #" + tag
#     # if (tweetStr + " #" + )
#     print(newTweet)


# def correctLength(tweetStr):
#     length = len(tweetStr)
#     if (length <)
#     return True

