word="donkey"
with open("xyz.txt","r") as f :
    content=f.read()

contentNew= content.replace(word,"######")

with open("xyz.txt","w") as f:
    f.write(contentNew)