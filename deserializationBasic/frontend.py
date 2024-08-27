import requests

URL = 'http://127.0.0.1:8000/create/'
data = {
    'name': "Student1",
    'roll': 101,
    'city': 'Mars',
}

# Correct way to send JSON data in a POST request
r = requests.post(url=URL, json=data)  # Use json= instead of data=

# Try to parse the response as JSON
try:
    response_data = r.json()
    print(response_data)
except requests.exceptions.JSONDecodeError:
    print("Failed to parse response as JSON. The response was:", r.text)
