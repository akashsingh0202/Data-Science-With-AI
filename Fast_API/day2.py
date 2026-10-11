from fastapi import FastAPI,Query,Path
import json

app = FastAPI()



class GetData():
    def get_data(self):
        with open ("data.json","r") as f:
            data =json.load(f)

        return data




# @app.get("/customers")
# def customers():
#     data=GetData()
#     customer=data.get_data()

#     return  customer

#  Query papameter
# @app.get("/city_data")
# def city_data(city:str):
#     data=GetData()
#     customers=data.get_data()

#     result=[]

#     for customer in customers :
#         if customer["city"]==city:
#             result.append(customer["age"])

#     return result



# @app.get("/major_age")
# def major_age(age:int,city:str):

#     data =GetData()
#     customers=data.get_data()
#     result=[]
#     for customer in customers:
#         if customer["age"]>age and customer["city"]==city:
#             result.append(customer)

#     return result



# @app.get("/customer_catogery")
# def customer_catogery(city:str=Query(...,description="pass the city name",example="Hyderabad"),
#                       category:str=Query(None),
#                       age:int=Query(None)
#                       ):

#     data=GetData()
#     customers=data.get_data()
#     result=[]
#     for customer in customers:
#         if customer["city"]==city and customer["age"]>=age or customer["category"]==category:
#             result.append({
#                 "customer_name":customer["customer_name"],
#                 "age":customer["age"],
#                 "category":customer['category']
#             })
#     return result



#  path parameter
# @app.get("/customers/{id}")
# def get_info(id:str=Path(...,description="pass the id ",example="C002")):
#     data=GetData()
#     customers=data.get_data()

#     for customer in customers :
#         if customer["customer_id"]==id:
#             return customer



@app.get("/demo/{category}")
def demo(category:str=Path(...),city:str=Query(...)):

    data=GetData()
    customers=data.get_data()

    for customer in customers :
        if customer['category']==category and customer['city']==city:
            return customer



