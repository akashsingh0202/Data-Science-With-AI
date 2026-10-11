from fastapi import FastAPI
import json

app=FastAPI()

class GetData:

    def get_data(self):
        with open ("data.json","r") as f:
            data =json.load(f)

        return data



@app.get('/')
def greet():
    return{'message': 'welcome to my website'}

@app.get('/info')
def information():
    return{'msg':'this is related to retail data'}


@app.get('/user_details')
def user_details():
    data=GetData()

    customers=data.get_data()

    return customers


# @app.get('/cities')
# def cities():
#     data =GetData()

#     customers=data.get_data()

#     return [
#         (cust['customer_name'],cust['city'] , cust['product'])
#         for cust in customers 
#         if cust['city']=='Bangalore' 
#         and cust['product']=='Laptop Bag' ]


# @app.get('/cities')
# def cities():
#     data = GetData()

#     customers = data.get_data()

#     return [
#         {
#             "city": cust["city"],
#             "product": cust["product"]
#         }
#         for cust in customers
#         if cust["city"] == "Mumbai"
#     ]


# @app.get('/cities')
# def city_info():
#     data = GetData()
#     customers=data.get_data()
#     return[(cust['city'],cust['customer_name'])for cust in customers if cust['city']=="Bangalore"]


@app.get('/cities')
def city_info(city:str):
    data = GetData()
    customers=data.get_data()

    result=[]

    for cust in customers:
        if cust['city']==city:
            result.append(cust['customer_name'])


    return result
            
        # return {'msg':'not found'}
    # return[(cust['city'],cust['customer_name'])for cust in customers if cust['city']=="Bangalore"]


# @app.get('/id')
# def get(id:str):
#     data=GetData()
#     customers=data.get_data()


#     # result=[]

#     for cust in customers:
#         if cust['customer_id']==id:
#             return cust
#     #         result.append(cust['customer_id'])

#     # return result

@app.get('/id')
def get(id: str):
    data = GetData()
    customers = data.get_data()

    for cust in customers:
        if cust['customer_id'] == id:
            return cust
            
    





