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

    # tweettopublish = 'However, before we are able to use the Twitter API end points, we need to create a developer account and generate our API keys. You can apply for a developer account directly here. After answering a few questions on how you plan to use the API and accept the Twitter Developer Agreement, you will be granted access to the Developer Dashboard. Once you are granted access to the dashboard, login to the developer site and create your first App. This step will automatically generate your consumer API keys and access tokens that you should keep secret:'

    # print(len(tweettopublish))

    # api.update_status(tweettopublish)
    # uncomment when ready to publish tweet

    # print(tweettopublish)

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

x = "Optimism is strength, pessimism is weakness. Based on which virtue you choose, your life is shaped. Those who chose positive attitude, can make wonder even out of adverse situations. Positivism helps as a booster when you take action. The Secret explains with Law of Attraction, the importance of positive thinking. If you learn to remain positive, you can cope with tough times easily. Your dreams can come true with a positive mindset. Let’s see what the famous people of the world have to say, through below mentioned quotes, about importance of positive thinking and positive attitude."
# x = "hi"
# print(len(x))
# # array = x.split(" ", 1)
# for part in array:
#     print(part)
# a = "(1/3) "
# print(len(a))
# publictweet()
initializeAPI()
createThread(x)
