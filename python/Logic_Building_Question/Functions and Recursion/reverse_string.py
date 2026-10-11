text=input("enter u r name : ")



def reverse(text):
     reverse="" 
     for char in text:
        reverse=char +reverse
     return(reverse)


print(reverse(text))
