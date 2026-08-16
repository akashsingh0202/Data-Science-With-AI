# mobile_info = {
    # 'name' : 'realme',
    # 'price':';32000',
    # 'Rating':4.5,
    # 'Discount':'25%'
# }
# print(mobile_info['name'])

mobiles = [
{
    'name' : 'realme',
    'price':'32000',
    'Rating':4.5,
    'Discount':'25%',
    'review': [
        {
            'name': 'sandeep',
            'rating':3.5,
            'problem':'heating'
        },

        {
            'name':'akash',
            'rating':4.5,
            'problem':'battery backup'

        }
    ]
 },
 {
      'name' : 'realme',
      'price':'32000',
      'Rating':4.7,
      'Discount':'25%'
 },

{
    'name' : 'realme',
    'price':'32000',
    'Rating':4.6,
    'Discount':'25%'
}
]
print(len(mobiles))
print(mobiles[0]['review'][1]['rating'])