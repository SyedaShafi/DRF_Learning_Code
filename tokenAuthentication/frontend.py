import requests
import json

URL = "http://127.0.0.1:8000/apis/"
URL_GET_TOKEN = "http://127.0.0.1:8000/gettoken/"

def getToken():
    data = {
        'username': 'user2',
        'password': 'shafi12345@'
    }
    header = {'content-Type': 'application/json'}
    r = requests.post(url = URL_GET_TOKEN, headers=header, json = data)
    try:
        response_data = r.json()
        return (response_data)
    except requests.exceptions.JSONDecodeError:
        return ("Failed to parse response as JSON. The response was:", r.text)

    


def getData(id = None):
    tokenData = getToken()
    data = {}
    if id is not None:
        data = {'id':id}
    header = {'content-Type': 'application/json', 'Authorization': f'Token {tokenData["token"]}'}
    r = requests.get(url=URL, headers=header, json = data)
    data = r.json()
    print(data)


def postData():
    tokenData = getToken()
    data = {
        'name': 'eka',
        'roll': 102,
        'city': 'Sunamganj',
    }
    header = {'content-Type': 'application/json', 'Authorization': f'Token {tokenData["token"]}'}
    r = requests.post(url = URL, headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)

def updateData():
    tokenData = getToken()
    data = {
        'id': 1,
        'name': 'Ekaaa Rani Rooooy',
        'roll': 107,
        'city': 'Sylhet',
    }
    header = {'content-Type': 'application/json', 'Authorization': f'Token {tokenData["token"]}'}
    r = requests.put(url = f'{URL}{data['id']}/', headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)


def deleteData():
    tokenData = getToken()
    data = {
        'id': 4
    }
    header = {'content-Type': 'application/json', 'Authorization': f'Token {tokenData["token"]}'}
    r = requests.delete(url = f"http://127.0.0.1:8000/apis/{data['id']}/", headers=header, json = data)
    if r.status_code == 204:
        print("Delete successful.")
    else:
        try:
            response_data = r.json()  # Only parse JSON if there is a response body
            print(response_data)
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to parse response as JSON. The response was: {r.text}")


# getData()
# postData()
# updateData()
# deleteData()
# getToken()