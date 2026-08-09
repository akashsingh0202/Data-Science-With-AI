#data types
#simple data types/user defined 
str='hii'
print(type(str))
int=123
print(type(int))
floate=123.34
print(type(floate))
bool=True
print(type(bool))

#Complex data types
#list
employee=['akash','anshul','me']
print(employee)
print(employee[0])
employee.append('subham')
print(employee)

matrix = [
[1, 3],
[3, 4]
]
print(matrix[1][1])

#Dictionary
product_info = {
    'name':'vivo',
    'rating': 4,
    'price' : 40000,
    'dicount': 80

}
print(product_info['name'])