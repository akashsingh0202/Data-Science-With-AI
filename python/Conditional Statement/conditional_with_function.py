age=int(input('enter ur age: '))

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
    
print(check_age(age))



num=int(input('enter a num: '))

def check_number(num):
    if num > 0:
        return "Positive"

    return "Not positive"

print(check_number(num))