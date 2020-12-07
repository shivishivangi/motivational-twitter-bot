#print("hi betch")

#NOTES:
#main.py will utilize these methods 

#   TWEETS:
#   randomize using web scrapping or the quotes database
#   add a method that tweets a certain amount of quotes
#   add a method that schedules tweets throughout the day
#   add a method that handles creating a tweet thread
#   add a hastag to the beginning of a quote (#MotivationalQuotes)

#   LIKES AND REPLIES:
#   like, retweet, and reply to people with the #MotivationalQuotes (make it possible to change this) hashtag
#   method to like a certain number of random tweets with a certain hashtag

#limitations:
#  needs to be less than 280 characters
#  if the tweet allows space, needs to include the hashtag with the category

#NOTE: try to figure out if you can make a thread 

import tweepy
import datetime

# need to make this a user input function 

consumer_key = 'UAEJdRp7QchFYpCUo5mfYoKpV'
consumer_secret = 'Gw2Rz6RQpXwLwmDcQgkaDrfgW6GSjm6G6Z37lXseDnGOpMoRXu'
access_token = '1331845784631975937-I6G0229akgSI6glrdaSyqaEeu8UqfX'
access_token_secret = 's54y03WQj7zcmWMDgjcwLZrnLVf0KLbXZz8ux4z4A6KVt'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
        tweettopublish = 'I love you Amulya'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Great it is Saturday #weekend #Saturday'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '

    #tweettopublish = 'However, before we are able to use the Twitter API end points, we need to create a developer account and generate our API keys. You can apply for a developer account directly here. After answering a few questions on how you plan to use the API and accept the Twitter Developer Agreement, you will be granted access to the Developer Dashboard. Once you are granted access to the dashboard, login to the developer site and create your first App. This step will automatically generate your consumer API keys and access tokens that you should keep secret:'

    print(len(tweettopublish))

    api.update_status(tweettopublish)
    #uncomment when ready to publish tweet
    print(tweettopublish)

publictweet()

def hashtag(tweetStr):

    newTweet = tweetStr + " #Motivating"
    size = len(newTweet)

    if (size <= 292 and size > 280):
        return tweetStr
    else: 
        return newTweet

    print(newTweet)
