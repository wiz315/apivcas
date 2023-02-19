import requests
import json


def barToken():
    auth_url = "https://www.textverified.com/Api/SimpleAuthentication"
    headers = {"Content-Type": "application/json; charset=utf-8", 'X-SIMPLE-API-ACCESS-TOKEN': "1_HgmSsAji0rISVwkYiFo6hFY0UjbynvCMbgb8dOtMSWPvQ1SbDaEUOW62vG0DjSivDHP"}
    response = requests.post(auth_url, headers=headers, ).json()
    response = response['bearer_token']
    return response

def getOneService(id , token):
    url = f"https://www.textverified.com/api/Targets/" + id
    headers = {"Authorization": "Bearer "+token, "Content-Type": "application/json; charset=utf-8"}
    response = requests.get(url, headers=headers).json()
    targetId = response['targetId']
    name = response['name']
    cost = response['cost']
    status = response['status']
    return targetId , name, cost, status

