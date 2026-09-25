f=open("myyy.txt","r")
data =f.readline()
# data =f.readlines()
while(data!=""):
    print(data)
    data=f.readline()
f.close()