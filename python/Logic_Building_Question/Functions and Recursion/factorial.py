a=int(input("Enter a number : "))
def fact(a):

    result=1

    for i in range(1,a+1):
        result=result*i


    return(result)

print(fact(a))