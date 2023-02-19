from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from db import ope
from timeHelper import timeNow, nextOrderTime
from helper import random_with_N_digits
app = FastAPI()

config = dotenv_values(".env")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")



@app.post("/api/createuser")
def cruser(firstname: str, midname: str, lastname: str, phone: str, email: str, verify: str, username, state: str, badg: str):
    data = ope.createUser(firstname, midname, lastname, phone, email,username, verify, state,badg)

    return {"message": "done"}

@app.post("/api/newOrder")
def newOrder(userId, type, card,price, delar ,amount, delarprice,usernote, adminnote, finish,delarnote):
    orderId = random_with_N_digits(6)
    createdate = timeNow()
    finsihdate = nextOrderTime(int(finish))
    status = "انتظار"
    data = ope.createOrder(userId, orderId, type, card,price, delar ,amount, delarprice,createdate, finsihdate, status,usernote, adminnote, delarnote)
    return {"message": "done","OrderId": orderId}

@app.get("/api/getorderbtuserId")
def getbyuserid(id):
    data = ope.findOrderbyUserId(int(id))
    return {"message": "done" , "orders": [data]}
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
