num = int(input('enter a number : '))
if num>0:
    if num%2==0:
        print('Even No.',num)
    else:
        print('odd no',num)
else:
    if num==0:
        print('number is zero')
    else:
        print('number is negative')