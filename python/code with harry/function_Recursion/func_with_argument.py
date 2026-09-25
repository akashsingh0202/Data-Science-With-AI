def heyy(names):
    print(f"heyyy {names}"  )

heyy("akash")

def heyyy(a,b):
    sum=a+b
    print(sum)

a=int(input("enter a number :"))
b=int(input("enter a number :"))
heyyy(a,b)


def intro(name , age):
    print(f"my name is {name}")
    print(f"my age is {age}")
    return "Done"

name= input("enter ur name :")
age = int(input("enter ur age :"))

a=intro(name,age)
print(a)