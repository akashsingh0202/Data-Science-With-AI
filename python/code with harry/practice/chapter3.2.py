# from datetime import datetime
# name= input("enter ur name :")
# date = input("Enter date (DD-MM-YYYY): ")
# date=datetime.strptime(date,"%d%m%Y").date()

# letter =(f'''Dear {name}
# you are selected 
# {date}''')

# print(letter)


letter=''' dear <|Name|>, your are selected!
<|date|>'''
print(letter.replace('<|Name|>',"akash").replace("<|date|>","05 sept 2026"))
