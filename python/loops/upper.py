s = 'asdfghjklw34e5rtyuioASDFGHJRFGHNG!@#$%^&*123456786543211234'
upper=0
lower=0
digit=0
special=0

for i in s:
    if i>='a' and i<='z':
        lower+=1
    elif i>='A' and i<='Z':
        upper+=1
    elif i>='0' and i<='9':
        digit+=1
    else:
        special+=1

print('upper:',upper, 'lower:',lower,'digit :',digit, 'special :',special )

