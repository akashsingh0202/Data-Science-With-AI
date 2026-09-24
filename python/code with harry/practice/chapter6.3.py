t1="Make a lot of money"
t2="buy now"
t3="subscribe this"
t4="click this"

message = input("Generate some message :")

if((message in t2) or( message in t3) or (message in t1) or( message in t4) ):
    print("Alert this is spam message")

else:
    print("not spam")