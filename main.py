import requests
import datetime as dt
today = dt.datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"
HABIT_API_KEY= "*****"
USER_NAME = "techjawn"
user_parameters ={
    "token": HABIT_API_KEY,
    "username": USER_NAME,
    "agreeTermsOfService": 'yes',
    "notMinor": "yes"
}
graph_parameters ={
    "id": "graph1",
    "name": "Steps Ahead",
    "unit": "miles",
    "type": "int",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": HABIT_API_KEY
}
graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'

pixs_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you complete today?"),
    "X-USER-TOKEN": HABIT_API_KEY
}
pixs_endpoint = f"{graph_endpoint}/graph1"
response = requests.post(url=pixs_endpoint, json=pixs_parameters,headers=headers)
print(response.text)
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# response = requests.post(url=pixs_endpoint, json=pixs_parameters, headers=headers)
# update_info = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_info, json=put_parameters, headers=headers)
# print(response.text)
# delete_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime("%Y%m%d")}'
# response = requests.delete(url=delete_endpoint,  headers=headers)
# print(response.text)
# put_parameters = {
#     "quantity": "12"
# }

