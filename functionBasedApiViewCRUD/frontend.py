import requests
import json

URL = "http://127.0.0.1:8000/apis/"

def getData(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    header = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=header, json = data)
    data = r.json()
    print(data)

def postData():
    data = {
        'name': 'muna',
        'roll': 104,
        'city': 'Sylhet',
    }
    header = {'content-Type': 'application/json'}

    r = requests.post(url = URL, headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)

def updateData():
    data = {
        'id': 1,
        'name': 'Ekaaa Rani Rooooy',
        'city': 'Sylhet',
    }
    header = {'content-Type': 'application/json'}

    r = requests.put(url = URL, headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)


def deleteData():
    data = {
        'id': 3
    }
    header = {'content-Type': 'application/json'}

    
    r = requests.delete(url = URL, headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)





    
# getData(2)
# postData()
# updateData()
deleteData()