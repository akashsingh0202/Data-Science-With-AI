words=["donkey","bad","nice"]
with open("xyz.txt","r") as f :
    content=f.read()

for word in words:
    content= content.replace(word,"#"*len(word))

with open("xyz.txt","w") as f:
    f.write(content)