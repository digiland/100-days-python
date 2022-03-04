from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "sirdiggaz"
TOKEN = "pixela_token"


# create_user_account
user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.status_code)
# print(r.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Minutes Read",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(r.text)

add_point = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/"

today = datetime.now().strftime("%Y%m%d")
add_params = {
    "date": today,
    "quantity": input("How many minutes did you read today? ")
}

r = requests.post(url=add_point, json=add_params, headers=headers)
print(r.text)


print(today)
