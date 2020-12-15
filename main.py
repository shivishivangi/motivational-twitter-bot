import datetime
import motivationalTwitterBot
import webScraping
import quotesFile

from random import randrange

motivationalTwitterBot.initializeAPI()

def randomTweets(rand):
    # possible quote sources: 
    # 1. webScraping.py getQuote()
    # 2. quotesFile.py getDataCSV() 
    # 3. quotesFile.py getMemeData()

    if (rand == 0):
        # tweettopublish = "Today's focus is #motivational quotes"
        # motivationalTwitterBot.publictweet(tweettopublish)
        for x in range(3):
            tweet = webScraping.getQuote()
            if (len(tweet) <= 280):
                motivationalTwitterBot.tweetquote(tweet)
            else:
                motivationalTwitterBot.createThread(tweet)

    if (rand == 1):
        # tweettopublish = "Today's focus is #inspiring quotes"
        # motivationalTwitterBot.publictweet(tweettopublish)
        for x in range(3):
            tweet = quotesFile.getDataCSV()
            if (len(tweet) <= 280):
                motivationalTwitterBot.tweetquote(tweet)
            else:
                motivationalTwitterBot.createThread(tweet) 

    if (rand == 2):
        # tweettopublish = "Today's focus is #meme quotes from this supposed mOtiVaTioNaL quotes database"
        # motivationalTwitterBot.publictweet(tweettopublish)
        # tweettopublish = "They be hella weird quotes tbh"
        # motivationalTwitterBot.publictweet(tweettopublish)
        for x in range(3):
            tweet = quotesFile.getMemeData()
            if (len(tweet) <= 280):
                motivationalTwitterBot.tweetquote(tweet)
            else:
                motivationalTwitterBot.createThread(tweet)

def morningMessage():
    if datetime.date.today().weekday() == 0:
        tweettopublish = "Happy Monday Morning!!! Start your week off right with some motivational quotes :)"
        motivationalTwitterBot.publictweet(tweettopublish)

    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday! Get sh*t done this week :) #productive'
        motivationalTwitterBot.publictweet(tweettopublish)
        
    if datetime.date.today().weekday() == 2:
        tweettopublish = "It's #Wednesday my dudesssss AAAAAAAAAAAHHHHHH #vine"
        motivationalTwitterBot.publictweet(tweettopublish)

    if datetime.date.today().weekday() == 3:
        tweettopublish = 'We are on the last stretch of the week. Tomorrow is Friday hehe I cannot wait for the weekend'
        motivationalTwitterBot.publictweet(tweettopublish)

    if datetime.date.today().weekday() == 4:
        tweettopublish = "Guess what? IT'S FINALLY FRIDAY!"
        motivationalTwitterBot.publictweet(tweettopublish)

    if datetime.date.today().weekday() == 5:
        tweettopublish = "Hope you had a fun Friday night. Chug some water and enjoy your weekend! #Saturday"
        motivationalTwitterBot.publictweet(tweettopublish)

    if datetime.date.today().weekday() == 6:
        tweettopublish = "Enjoy your chill Sunday morning hehe you've got a productive week ahead of you!"
        motivationalTwitterBot.publictweet(tweettopublish)

def publishQuotes():
    random = randrange(0, 100000)
    randomTweets(random%3)



if datetime.date.today().weekday() == 0:
    # tweettopublish = "Happy Monday Morning!!! Start your week off right with some motivational quotes :)"
    # motivationalTwitterBot.publictweet(tweettopublish)
    random = randrange(0, 100000)
    randomTweets(random%3)

if datetime.date.today().weekday() == 1:
    # tweettopublish = 'Enjoy your Tuesday! Get sh*t done this week :) #productive'
    # motivationalTwitterBot.publictweet(tweettopublish)
    random = randrange(0, 100000)
    # randomTweets(random%3)
    # print(datetime.datetime.now())
    
if datetime.date.today().weekday() == 2:
    # tweettopublish = "It's #Wednesday my dudesssss AAAAAAAAAAAHHHHHH #vine"
    # motivationalTwitterBot.publictweet(tweettopublish)
    random = randrange(0, 100000)
    randomTweets(random%3)

if datetime.date.today().weekday() == 3:
    # tweettopublish = 'We are on the last stretch of the week. Tomorrow is Friday hehe I cannot wait for the weekend'
    random = randrange(0, 100000)
    randomTweets(random%3)

if datetime.date.today().weekday() == 4:
    # tweettopublish = "Guess what? IT'S FINALLY FRIDAY!"
    random = randrange(0, 100000)
    randomTweets(random%3)

if datetime.date.today().weekday() == 5:
    # tweettopublish = "Hope you had a fun Friday night. Chug some water and enjoy your weekend! #Saturday"
    random = randrange(0, 100000)
    randomTweets(random%3)

if datetime.date.today().weekday() == 6:
    # tweettopublish = "Enjoy your chill Sunday morning hehe you've got a productive week ahead of you!"
    random = randrange(0, 100000)
    randomTweets(random%3)
    # motivationalTwitterBot.purgeTweets(7)

