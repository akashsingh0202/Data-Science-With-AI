# from fastapi import FastAPI
# import json


# class GetData:
#     def get_data(self):
#         with open("data.json","r") as f:
#             data=json.load(f)

#         return data

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated



class Customers(BaseModel):
    name:Optional[str] = None
    Email:EmailStr
    age:Annotated[int,Field(gt=30,description="age must be greater than 30",examples=[30,30,40])]=0
    products:List[str]
    cart:Dict[str,int]
    url:AnyUrl
    price:Annotated[int,Field(strict=True)]

def insert(cust:Customers):
    print(cust.name)
    print(cust.Email)
    print(cust.age)
    print(cust.products)
    print(cust.cart)
    print(cust.url)
    print(cust.price+10000)


data={
      'name':'akash','Email':'akashsingh@gmail.com',"age":31,'products':['ashu','Akash'],'cart':{'groceries':34500},'url':'http://www.google.com/','price':30000}

customer1=Customers(**data)

insert(customer1)


