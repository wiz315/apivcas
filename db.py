from pymongo import MongoClient
import pymongo
from timeHelper import timeNow, nextOrderTime
from pandas import DataFrame
client = MongoClient("mongodb+srv://cash:yazz313YGCAH@cluster0.2g7of4m.mongodb.net/?retryWrites=true&w=majority",)
db = client.cash
user = db.user

try:
    conn = client

    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  

class ope():
    def createUser(userid,firstname, midname,lastname, phone, email, verify, state, username, badg):
        data = {
            "userId": userid,
            "fname": firstname,
            "mname": midname,
            "lastname": lastname,
            "phone": phone,
            "email": email,
            "ver": verify,
            "state": state,
            "username": username,
            "badg": badg
        }
        user = db.user.insert_one(data)
        return user
# found user
    def findUsers():
        a = list(db["user"].find({}))
        return a
#create order 
    def createOrder(userId, orderId, type, card,price, delar ,amount, delarprice,createDate, finishDate, status,usernote, adminnote, delarnote):
        data = {
            "userID": userId,
            "orderId": orderId,
            "type": type,
            "card": card,
            "price":price,
            "amount": amount,
            "delar": delar,
            "delarprice": delarprice,
            "createDate": createDate,
            "finishDate": finishDate,
            "status": status,
            "userNote": usernote,
            "adminNote": adminnote,
            "delarNote": delarnote,
        }
        order = db.orders.insert_one(data)
        return order
#find all order
    def findOrderbyUserId(userId):
        data = list(db["orders"].find({"userID": { "$eq": userId }} ,{'_id': 0}))
        return data
#find one order by order id
    def findOrderbyOrderID(orderID):
        data = db['orders'].find({"orderId": {"$eq": orderID}})
        for doc in data:
            return doc
    
    def findlastorder(userID):
        data = db['orders'].find({"userID": {"$eq": userID}},{'_id': 0}).sort("_id", -1 )
        for doc in data:
            return doc
