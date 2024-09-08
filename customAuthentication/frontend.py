import requests
import json

URL = "http://127.0.0.1:8000/apis/"

def getData(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    params = {'username': 'superuser'}
    r = requests.get(url=f'{URL}{id}/', json = data, params=params)
    data = r.json()
    print(data)

def postData():
    data = {
        'name': 'Ekaaa',
        'roll': 104,
        'city': 'Sylhet',
    }
    params = {'username': 'superuser'}
    r = requests.post(url = URL, json = data, params=params)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)

def updateData():
    data = {
        'id': 3,
        'name': 'Ekaaa Rani Roy',
        'city': 'Sylhet',
    }
    params = {'username': 'superuser'}
    r = requests.patch(url = f'{URL}{data['id']}/', json = data, params=params)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)


def deleteData():
    data = {
        'id': 4
    }
    params = {'username': 'superuser'}
    r = requests.delete(url = f'{URL}{data['id']}/', json = data, params=params)
    if r.status_code == 204:
        print('Delete successful.')
    else:
        try:
            response_data = r.json()
            print(response_data)
        except requests.exceptions.JSONDecodeError:
            print("Failed to parse response as JSON. The response was:", r.text)





    
# getData(2)
# postData()
# updateData()
deleteData()