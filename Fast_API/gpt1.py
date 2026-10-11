from fastapi import FastAPI
import json
app=FastAPI()

class GetData:
    def get_data(self):
        with open("data.json","r") as f:
            data=json.load(f)

        return data


# @app.get('/customers')
# def get_customers():
#     return{"message":"All Customers"}

# @app.get('/')
# def home():
#     return{"message":"hello fast api"}


# @app.get('/products')
# def get_product():
#     return {"message":"All Products"}




# @app.get("/customers")
# def get_customers():
#     data=GetData()
#     customers=data.get_data()

#     return customers


# @app.get("/customer_name")
# # def get_customer(customer_name:str):
# def get_customer():
#     data=GetData()
#     customers=data.get_data()

#     names=[]

#     for customer in customers: 
#         # if customer["customer_name"]==customer_name:
#             names.append(customer['customer_name'])
      

#     return names


# @app.get("/customer_name")
# def get_customer_name():
#     data=GetData()
#     customers=data.get_data()

#     names=[]
#     for customer in customers:
#         names.append(customer["customer_name"])

#     return names


# @app.get("/customer_name")
# def get_customer_name():


#     data=GetData()
#     customers=data.get_data()


#     customer_name=customers[0]["customer_name"]

#     return customer_name



# @app.get("/customer_name")
# def customer_name():

#     data=GetData()
#     customers=data.get_data()

#     customer_names=[]

#     for customer in customers:
#         customer_names.append(customer["customer_name"])


#     return customer_names



# @app.get("/customer/{customer_id}")
# def get_customer(customer_id:str):

#     data=GetData()
#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return customer


# @app.get("/customer/{customer_id}")
# def get_customer_name(customer_id:str):

#     data=GetData()

#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return customer["customer_name"]



# @app.get("/customer/{customer_id}")

# def user_info(customer_id:str):

#     data=GetData()
#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return {
#                 "customer_name":customer["customer_name"],
#                 "city":customer["city"]
#             }
            # return (customer["customer_name"],customer["city"])


# @app.get("/customer/{customer_id}")

# def user_info(customer_id:str):

#     data=GetData()
#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return {
#                 "customer_name":customer["customer_name"],
#                 "city":customer["city"]
#             }

#     return {"msg":"not found"}



# Query Parameter

# @app.get("/customer")
# def get_customer(customer_id: str):
#     data=GetData()
#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return customer



# @app.get("/customer")
# def get_customer(customer_id: str):
#     data=GetData()
#     customers=data.get_data()

#     for customer in customers:
#         if customer["customer_id"]==customer_id:
#             return {
#                 "customer_name":customer["customer_name"],
#                 "city":customer["city"]
#             }


# @app.get("/customer")
# def get_city(city:str):
#      data=GetData()
#      customers=data.get_data()

#      result=[]

#      for customer in customers:
#          if customer["city"]==city:

#              result.append({
#                  "customer_name":customer["customer_name"],
#                  "city":customer["city"]
#              })


#      return result


# @app.get("/customer")
# def userinfo(city:str,customer_name:str):

#     data=GetData()
#     customers=data.get_data()


#     for customer in customers:
#         if customer["city"] == city and customer["customer_name"] == customer_name:
#          return customer





#optional query parameter 

# @app.get("/customer")
# def userinfo(city: str | None = None):

#     data = GetData()
#     customers = data.get_data()

#     if city is None:
#         return customers

#     result = []

#     for customer in customers:
#         if customer["city"] == city:
#             result.append(customer)

#     return result                            
            #      "city":customer["city"]})
            #  return {
            #      "customer_name":customer["customer_name"],
            #      ""customer_name":customer["customer_name"],
            #      "city":customer["city"]

            #  }


        
# @app.get("/customer")
# def get_city(city:str|None=None):
#     data=GetData()
#     customers=data.get_data()

#     if city is None:
#         return customers

#     result=[]

#     for customer in customers :
#         if customer["city"]==city:
#             result.append({
#                 "customer_name":customer["customer_name"],
#                 "city":customer["city"]
#             })

#     return result


# @app.get("/customer")
# def user_detect(customer_name:str|None=None):

#     data=GetData()
#     customers=data.get_data()


#     if customer_name is None:
#         return customers

#     result=[]

#     for customer in customers :
#         if customer["customer_name"]==customer_name:
#             result.append({
#                 "customer_name":customer["customer_name"],
#                 "city":customer["city"],
#                 "product":customer["product"]
#             })


#     return result



# @app.get("/customer")
# def cust_info(customer_name:str|None=None , city:str|None=None):
#     data=GetData()
#     customers=data.get_data()

#     result=[]


#     for customer in customers:


#         if customer_name is None and city is None:
#             result.append(customer)

#         elif customer_name is None:
#             if customer["city"]==city:
#                 result.append({
#                     "city":customer["city"]
#                 })
#         elif city is None :
#             if customer["customer_name"]==customer_name:
#                 result.append({
#                     "customer_name":customer["customer_name"]
#                 })


#         else:
#             if customer["customer_name"]==customer_name and customer["city"]==city:
#                 result.append({
#                     "customer_name":customer["customer_name"],
#                     "city":customer["city"],
#                     "product":customer["product"]
#                 })

#     return result



#  path + query parameter



@app.get("/customer/{city}")
def get_info(city:str,customer_name:str|None=None):
    data=GetData()
    customers=data.get_data()

    result=[]

    for customer in customers:
        if customer_name is not None:

            if customer["city"]==city and customer["customer_name"]==customer_name:
                result.append(customer)


        else:
            if customer["city"]==city:
                result.append(customer)

    return result



