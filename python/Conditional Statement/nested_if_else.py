marks=int(input('enter your marks: '))
name=input('enter your name : ')
scholarship=0

if marks>=90:
 print('A')
 scholarship+=30
 print(f'heyy {name} congratulations')
 print(f'you are eligible for {scholarship} percent scholarship')

elif marks>=70 :
 print('B')
 scholarship+=20
 print(f'hi {name} congratulations')
 print(f'you are eligible for {scholarship} percent scholarship')

elif marks >=60 :
 print('C')
 scholarship+=10
 print(f'hii {name} congratulations')
 print(f'you are eligible for {scholarship} percent scholarship')


else:
 print(f'sorry {name} U R fail')
 print('u R not elegible for scholarship')
 