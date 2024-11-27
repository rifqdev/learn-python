import requests
from datetime import datetime

PIXELA_API = "https://pixe.la/v1/users"
TOKEN = "abc123"
USERNAME = "abc123"
GRAPHID = "abc123"


# payload = {
#     "token": "dfdsfhsfhdsfgsdfsdsdf",
#     "username": "rifq",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=PIXELA_API, json=payload)

graph_api = f"{PIXELA_API}/{USERNAME}/graphs"

payload = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_api, json=payload, headers=headers)


post_graph_value_api = f"{PIXELA_API}/{USERNAME}/graphs/{GRAPHID}"

day = datetime(year=2024, month=11, day=26)
date = day.strftime("%Y%m%d")

payload = {
    "date": date,
    "quantity": "19"
}

# response = requests.post(url=post_graph_value_api, json=payload, headers=headers)
# print(response.text)


update_pixel_value_api = f"{PIXELA_API}/{USERNAME}/graphs/{GRAPHID}/{date}"

payload = {
    "quantity": "30"
}

# response = requests.put(url=update_pixel_value_api, json=payload, headers=headers)
# print(response.text)

delete_pixel_value_api = f"{PIXELA_API}/{USERNAME}/graphs/{GRAPHID}/{date}"

# response = requests.delete(url=delete_pixel_value_api, headers=headers)
# print(response.text)