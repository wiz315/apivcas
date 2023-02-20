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
    data = ope.findOrderbyUserId(id)
    return {"message": "done" , "orders": [data]}

@app.get("/api/lastorder")
def lastorder(id):
    data = ope.findlastorder(id)
    return {"order": data}

# create delars
@app.post("/api/createDelars")
def createOrders(delarOneName, delarOneAdress, delarOnePlace, delarOnePhone, delarOneMap,delarTwoName, delarTwoAddress,
                    delarTwoPlace, delarTwoPhone, delarTwoMap, delarThreeName, delarThreeAddress, delarThreePlace, delarThreePhone, delarThreeMap,
                    delarFourName, delarFourAddress, delarFourPlace, delarFourPhone, delarFourMap, delarFiveName, delarFiveAddres, 
                    delarFivePlace, delarFivePhone, delarFiveMap, delarSixName, delarSixAddress, delarSixPlace, delarSixPhone,
                    delarSixMap, delarSevenName, delarSevenAddress, delarSevenPlace, delarSevenPhone, delarSevenMap,
                    delarEightName, delarEightAddress, delarEightplace, delarEightPhone, delarEightMap,
                    delarNineName, delarNineAddress, delarNinePlace, delarNinePhone, delarNineMap,
                    delarTenName, delarTenAddress, delarTenPlace, delarTenPhone, delarTenMap,
                    delarElevenName, delarElevenAddress, delarElevenPlace, delarElevenPhone, delarElevenMap) :
                    data = ope.newDelars(delarOneName, delarOneAdress, delarOnePlace, delarOnePhone, delarOneMap,delarTwoName, delarTwoAddress,
                    delarTwoPlace, delarTwoPhone, delarTwoMap, delarThreeName, delarThreeAddress, delarThreePlace, delarThreePhone, delarThreeMap,
                    delarFourName, delarFourAddress, delarFourPlace, delarFourPhone, delarFourMap, delarFiveName, delarFiveAddres, 
                    delarFivePlace, delarFivePhone, delarFiveMap, delarSixName, delarSixAddress, delarSixPlace, delarSixPhone,
                    delarSixMap, delarSevenName, delarSevenAddress, delarSevenPlace, delarSevenPhone, delarSevenMap,
                    delarEightName, delarEightAddress, delarEightplace, delarEightPhone, delarEightMap,
                    delarNineName, delarNineAddress, delarNinePlace, delarNinePhone, delarNineMap,
                    delarTenName, delarTenAddress, delarTenPlace, delarTenPhone, delarTenMap,
                    delarElevenName, delarElevenAddress, delarElevenPlace, delarElevenPhone, delarElevenMap)
                    return {"delars" : "done"}

# get delars
@app.get("/api/delars")
def lastorder():
    data = ope.delars()
    return {"delars": data}
    
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
