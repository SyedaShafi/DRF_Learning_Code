import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def getData(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    r = requests.get(url=URL, json = data)
    data = r.json()
    print(data)

def postData():
    data = {
        'name': 'muna',
        'roll': 104,
        'city': 'Sylhet',
    }
    r = requests.post(url = URL, json = data)
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
    r = requests.put(url = URL, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)


def deleteData():
    data = {
        'id': 3
    }
    r = requests.delete(url = URL, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)





    
# getData()
postData()
# updateData()
# deleteData()