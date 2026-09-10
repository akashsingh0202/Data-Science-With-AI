# signup
user = 'akash'
password='12345'

#sign in
user_name = input('enter your user name :').lower()
user_password=input('eneter your password :')

if user==user_name and password==user_password:
    print('************************************')
    print(f'login successfully , welcome {user}')
    print('***************************************')
    total=int(input('enter your bill: '))
    print('************************************')
    print(f'Your total bill is {total}')
    if total>=10000:
        discount=total*0.2
        final_price=total-discount
        print(f'you have get discount : {discount}')
        print(f'your final bill is {final_price}')

    elif total>=5000:
         discount=total*0.1
         final_price=total-discount
         print(f'you have get discount : {discount}')
         print(f'your final bill is {final_price}')

    elif total>=3000:
         discount=total*0.05
         final_price=total-discount
         print(f'you have get discount : {discount}')
         print(f'your final bill is {final_price}')

    else:
         print('you are not elligible for discount')


else:
     print('incorrect username and  password')
         