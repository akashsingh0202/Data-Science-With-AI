from fastapi import FastAPI
import json


app = FastAPI()

# @app.get("/info")
# def information():
#     return {
#         "name": "Akash",
#         "course": "FastAPI",
#         "status": "learning"
#      }


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


@app.get("/info")
def information():
    return {
        "course": "FastAPI",
        "topic": "JSON Response"
    }