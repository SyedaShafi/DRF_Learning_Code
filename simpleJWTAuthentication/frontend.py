import requests
import json
# This refresh token is validated for 1 day

URL = "http://127.0.0.1:8000/apis/"
URL_GETTOKEN = "http://127.0.0.1:8000/gettoken/"
URL_VERIFYTOKEN = "http://127.0.0.1:8000/verifytoken/"
URL_REFRESHTOKEN = "http://127.0.0.1:8000/refreshtoken/"


def gettoken():
    data = {
        'username': 'user1',
        'password': 'shafi12345@'
    }
    r = requests.post(url = URL_GETTOKEN, json = data)
    if r.status_code == 200:
        tokens = r.json()
        access_token = tokens.get('access')
        refresh_token = tokens.get('refresh')
        print('access token ===', access_token)
        print('refresh token === ', refresh_token)
    else:
        print(f'failed to get token: {r.status_code} - {r.text}')

def verifytoken():
    data = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDc4Nzc4LCJpYXQiOjE3MjU0NzgxOTQsImp0aSI6ImM3MGU2NWUzMWQ2NTQyYzZhNjViMzY5NzI1M2NjZjU5IiwidXNlcl9pZCI6Mn0.9ut4rgKERDIvsG8AfrCdZTNwPLvU6jytqD_UMnCByYg',
    }
    r = requests.post(url = URL_VERIFYTOKEN, json=data)
    if r.status_code == 200:
        tokens = r.json()
        print('token is validated: ', tokens)
    else:
        print(f'failed to get token: {r.status_code} - {r.text}')

def refreshtoken():
    data = {
        'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2NDU5NCwiaWF0IjoxNzI1NDc4MTk0LCJqdGkiOiJjOGY1ZTVmNDE5YjM0MzUwYjc2ZGFlYTU5OGIwOTAzZiIsInVzZXJfaWQiOjJ9.Wqldt2zIIIcPUsqBOSrHuaFJ2br5K17v-Tup-8Pn5EE',
    }
    r = requests.post(url = URL_REFRESHTOKEN, json=data)
    if r.status_code == 200:
        tokens = r.json()
        # print('New access token: ', tokens.get('access'))
        return tokens.get('access')
    else:
        # print(f'Failed to get token: {r.status_code} - {r.text}')
        return None

def getData(id = None):
    data = {}
    URL = 'http://127.0.0.1:8000/apis/'
    if id is not None:
        data = {'id':id}
        URL = f'http://127.0.0.1:8000/apis/{id}/'
    token = refreshtoken()
    # print(token)
    if token is not None:
        header = {'Content-Type': 'application/json','Authorization': f'Bearer {token}'}
        r = requests.get(url=URL, headers=header, json = data)
        data = r.json()
        print(data)
    else:
        print('You need to use new refesh token')

def postData():
    data = {
        'name': 'Ekaaa',
        'roll': 104,
        'city': 'Sylhet',
    }
    token = refreshtoken()
    header = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    r = requests.post(url = URL,headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)

def updateData():
    data = {
        'id': 5,
        'name': 'Ekaaa Rani Roy',
        'city': 'Sylhet',
    }
    token = refreshtoken()
    header = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    r = requests.patch(url = f'{URL}{data['id']}/',headers=header, json = data)
    try:
        response_data = r.json()
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse response as JSON. The response was:", r.text)


def deleteData():
    data = {
        'id': 5
    }
    token = refreshtoken()
    header = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    r = requests.delete(url = f'{URL}{data['id']}/',headers = header, json = data)
    if r.status_code == 204:
        print('Delete successful.')
    else:
        try:
            response_data = r.json()
            print(response_data)
        except requests.exceptions.JSONDecodeError:
            print("Failed to parse response as JSON. The response was:", r.text)

# gettoken()  
# verifytoken()  
# refreshtoken()
# getData()
# postData()
# updateData()
# deleteData()