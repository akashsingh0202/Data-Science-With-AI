n=int(input("Enter a number"))
i=2
while(n%n==1):
    if(n%i==0):

      print(" not a prime no")
      break
    i+=1
else:
    print("prime number ")