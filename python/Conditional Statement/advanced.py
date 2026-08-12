age = int(input('enter ur age '))
salary = int(input('enter ur salary'))
experience = int(input('how many years experience u have'))

if age >= 18 and (salary >= 30000 or experience >= 2):
    print("Eligible")

else:
    print('Not eligible')