# motivationalTwitterBot.py

#NOTES:
#main.py will utilize these methods 

#   TWEETS:
#   add a method that tweets a certain amount of quotes
#   add a method that schedules tweets throughout the day

#   LIKES AND REPLIES:
#   like, retweet, and reply to people with the #MotivationalQuotes (make it possible to change this) hashtag
#   method to like a certain number of random tweets with a certain hashtag


import tweepy
import math
import datetime

from datetime import timedelta


# need to make this a user input function 
def initializeAPI():
    global api
    consumer_key = 'UAEJdRp7QchFYpCUo5mfYoKpV'
    consumer_secret = 'Gw2Rz6RQpXwLwmDcQgkaDrfgW6GSjm6G6Z37lXseDnGOpMoRXu'
    access_token = '1331845784631975937-I6G0229akgSI6glrdaSyqaEeu8UqfX'
    access_token_secret = 's54y03WQj7zcmWMDgjcwLZrnLVf0KLbXZz8ux4z4A6KVt'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


def publictweet(tweettopublish):

    try:
        api.update_status(tweettopublish)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            # Do something special
            print('duplicate message')
        else:
            raise error

def tweetquote(tweettopublish):

    tweettopublish = hashtag(tweettopublish)

    try:
        api.update_status(tweettopublish)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            # Do something special
            print('duplicate message')
        else:
            raise error

def replytweet(tweettopublish, tweetid):
    # global api

    try:
        api.update_status(tweettopublish, tweetid)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            # Do something special
            print('duplicate message')
        else:
            raise error


def hashtag(tweetStr):

    # adds #Motivating to tweet if adding it does not exceed 280 characters

    newTweet = tweetStr + " #Motivating"
    size = len(newTweet)

    if (size <= 292 and size > 280):
        return tweetStr
    else: 
        return newTweet
    

def createThread(tweet):
    # if tweet is more than 280 characters it separates it into multiple tweets 
    # creates a thread by replying to the previous tweet
    # need to keep track of that tweet id and then reply 

    length = len(tweet)
    index = 273
    count = 1 
    finalCount = math.ceil(length / 274)

    while (count <= finalCount):
        if (count == 1):
            strCount = "(1/" + str(finalCount) + ") "
            partTweet = tweet[0:273]
            if (partTweet[-1] == ' '):
                newTweet = strCount + partTweet 
                index = 274
            else: 
                while(partTweet[-1] != ' '):
                    index -= 1
                    partTweet = tweet[0:index]
                newTweet = strCount + partTweet 

            count += 1
            publictweet(newTweet)
            # api.update_status(newTweet)

        elif (count == finalCount):
            strCount = "(" + str(count) + "/" + str(finalCount) + ") "
            partTweet = tweet[index:length]
            newTweet = strCount + partTweet
            count += 1
            tweet = hashtag(newTweet)
            replytweet(tweet, getTweetID())
            # api.update_status(tweet, getTweetID())

        else: 
            strCount = "(" + str(count) + "/" + str(finalCount) + ") "
            newindex = index + 273
            partTweet = tweet[index:newindex]
            if (partTweet[-1] == ' '):
                newTweet = strCount + partTweet 
                index = newindex
            else: 
                while(partTweet[-1] != ' '):
                    newindex -= 1
                    partTweet = tweet[index:newindex]
                
                index = newindex
                newTweet = strCount + partTweet
        
            count += 1
            replytweet(newTweet, getTweetID())
            # api.update_status(newTweet, getTweetID())

        # print(newTweet)
        

def getTweetID():
    timeline = api.user_timeline("MotivateBot_")
    recent = timeline[0].id
    return recent

def purgeTweets(day):
    cutoff_date = datetime.datetime.utcnow() - timedelta(days=day)
    timeline = tweepy.Cursor(api.user_timeline).items()
 
    for tweet in timeline:
        if tweet.created_at > cutoff_date:
            api.destroy_status(tweet.id)
             
# initializeAPI()
# purgeTweets()