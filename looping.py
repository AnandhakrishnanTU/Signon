import datetime

current=datetime.datetime.now()
hour=int(current.strftime("%H"))

if(0<=hour<12):
    print("Good Morning")
elif(12<=hour<15):
    print("Good Afternoon")
elif(15<=hour<20):
    print("Good Evening")
elif(20<=hour<24):
    print("Good Night")