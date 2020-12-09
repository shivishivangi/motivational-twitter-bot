import datetime

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