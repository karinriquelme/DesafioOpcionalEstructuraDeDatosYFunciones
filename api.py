import requests
import json

url = "https://reqres.in/api/users"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

users_data = requests.get(url)
print(json.dumps(users_data.json(), sort_keys=True, indent=2), "\n")
print("codigo respuesta:", users_data.status_code)

data = {
    "nombre": "Ignacio",
    "trabajo": "profesor"
}

created_user = requests.post(url, json=data, headers=headers)
print(created_user.json())
print(created_user.status_code)

data = {
    "residence": "zion"
}

update_user = requests.put(url + "/username=Morpheus", json=data, headers=headers)
print(update_user.json())
print(update_user.status_code)

deleted_user = requests.delete(url + "/username=Tracey")
print(deleted_user.status_code)

# user=requests.get(url+"?id=4")
# print(user.json())
