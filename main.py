import datetime
import motivationalTwitterBot
import webScraping
import quotesFile

motivationalTwitterBot.initializeAPI()

if datetime.date.today().weekday() == 0:
    tweettopublish = 'Happy Meme Monday'
    motivationalTwitterBot.publictweet(tweettopublish)
    tweettopublish = "Today's focus is #meme quotes from this supposed mOtiVaTioNaL quotes database"
    motivationalTwitterBot.publictweet(tweettopublish)
    for x in range(11):
        tweet = quotesFile.getMemeData()
        if (len(tweet) <= 280):
            motivationalTwitterBot.tweetquote(tweet)
        else:
            motivationalTwitterBot.createThread(tweet)
    

if datetime.date.today().weekday() == 1:
    tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    motivationalTwitterBot.publictweet(tweettopublish)
    tweettopublish = "Today's focus is #inspiring quotes"
    motivationalTwitterBot.publictweet(tweettopublish)
    for x in range(11):
        tweet = quotesFile.getDataCSV()
        if (len(tweet) <= 280):
            motivationalTwitterBot.tweetquote(tweet)
        else:
            motivationalTwitterBot.createThread(tweet)  



if datetime.date.today().weekday() == 2:
    tweettopublish = "It's #Wednesday my dudesssss AAAAAAAAAAAHHHHHH #vine"
    motivationalTwitterBot.publictweet(tweettopublish)
    tweettopublish = "Today's focus is #positive quotes"
    motivationalTwitterBot.publictweet(tweettopublish)
    for x in range(11):
        tweet = webScraping.getQuote()
        if (len(tweet) <= 280):
            motivationalTwitterBot.tweetquote(tweet)
        else:
            motivationalTwitterBot.createThread(tweet) 

if datetime.date.today().weekday() == 3:
    tweettopublish = 'Thursday. I cannot wait for the Weekend'


if datetime.date.today().weekday() == 4:
    tweettopublish = 'Friday...Finally'


if datetime.date.today().weekday() == 5:
    tweettopublish = 'Great it is Saturday #weekend #Saturday'


if datetime.date.today().weekday() == 6:
    tweettopublish = 'Sunday morning...#Weekend #enjoy '