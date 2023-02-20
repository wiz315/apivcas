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
# 
    def findlastorder(userID):
        data = db['orders'].find({"userID": {"$eq": userID}},{'_id': 0}).sort("_id", -1 )
        for doc in data:
            return doc
# delars list
    def newDelars(delarOneName, delarOneAdress, delarOnePlace, delarOnePhone, delarOneMap,delarTwoName, delarTwoAddress,
                    delarTwoPlace, delarTwoPhone, delarTwoMap, delarThreeName, delarThreeAddress, delarThreePlace, delarThreePhone, delarThreeMap,
                    delarFourName, delarFourAddress, delarFourPlace, delarFourPhone, delarFourMap, delarFiveName, delarFiveAddres, 
                    delarFivePlace, delarFivePhone, delarFiveMap, delarSixName, delarSixAddress, delarSixPlace, delarSixPhone,
                    delarSixMap, delarSevenName, delarSevenAddress, delarSevenPlace, delarSevenPhone, delarSevenMap,
                    delarEightName, delarEightAddress, delarEightplace, delarEightPhone, delarEightMap,
                    delarNineName, delarNineAddress, delarNinePlace, delarNinePhone, delarNineMap,
                    delarTenName, delarTenAddress, delarTenPlace, delarTenPhone, delarTenMap,
                    delarElevenName, delarElevenAddress, delarElevenPlace, delarElevenPhone, delarElevenMap):
                        data = {
                            "delarOneName": delarOneName,
                            "delarOneAdress": delarOneAdress,
                            "delarOnePlace": delarOnePlace,
                            "delarOnePhone": delarOnePhone,
                            "delarOneMap": delarOneMap,
                            "delarTwoName": delarTwoName,
                            "delarTwoAddress": delarTwoAddress,
                            "delarTwoPlace": delarTwoPlace,
                            "delarTwoPhone": delarTwoPhone,
                            "delarTwoMap": delarTwoMap,
                            "delarThreeName": delarThreeName,
                            "delarThreeAddress": delarThreeAddress,
                            "delarThreePlace": delarThreePlace,
                            "delarThreePhone": delarThreePhone,
                            "delarThreeMap": delarThreeMap,
                            "delarFourName": delarFourName,
                            "delarFourAddress": delarFourAddress,
                            "delarFourPlace": delarFourPlace,
                            "delarFourPhone": delarFourPhone,
                            "delarFourMap": delarFourMap,
                            "delarFiveName": delarFiveName,
                            "delarFiveAddres": delarFiveAddres,
                            "delarFivePlace": delarFivePlace,
                            "delarFivePhone": delarFivePhone,
                            "delarFiveMap": delarFiveMap,
                            "delarSixName": delarSixName,
                            "delarSixAddress": delarSixAddress,
                            "delarSixPlace": delarSixPlace,
                            "delarSixPhone": delarSixPhone,
                            "delarSixMap": delarSixMap,
                            "delarSevenName": delarSevenName,
                            "delarSevenAddress": delarSevenAddress,
                            "delarSevenPlace": delarSevenPlace,
                            "delarSevenPhone": delarSevenPhone,
                            "delarSevenMap": delarSevenMap,
                            "delarEightName": delarEightName,
                            "delarEightAddress": delarEightAddress,
                            "delarEightplace": delarEightplace,
                            "delarEightPhone": delarEightPhone,
                            "delarEightMap": delarEightMap,
                            "delarNineName": delarNineName,
                            "delarNineAddress": delarNineAddress,
                            "delarNinePlace": delarNinePlace,
                            "delarNinePhone": delarNinePhone,
                            "delarNineMap": delarNineMap,
                            "delarTenName": delarTenName,
                            "delarTenAddress": delarTenAddress,
                            "delarTenPlace": delarTenPlace,
                            "delarTenPhone": delarTenPhone,
                            "delarTenMap": delarTenMap,
                            "delarElevenName": delarElevenName,
                            "delarElevenAddress": delarElevenAddress,
                            "delarElevenPlace": delarElevenPlace,
                            "delarElevenPhone": delarElevenPhone,
                            "delarElevenMap": delarElevenMap,
                        }
                        order = db.delar.insert_one(data)
                        return order
#
    def delars():
        data = db['delar'].find({},{'_id': 0})
        for doc in data:
            return doc
a = ope.delars()
print(a)