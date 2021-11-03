import requests
from datetime import datetime

# HTTP requests
# GET: requests.get()
# POST
# PUT
# DELETE

# https://pixe.la/
# https://docs.pixe.la/

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# set up user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# set up graph
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# headers:
graph_header = {
    "X-USER-TOKEN": TOKEN
}
# query:
graph_params= {
    "id":GRAPH_ID,
    "name":"movie time",
    "unit":"minutes",
    "type":"int",
    "color":"sora"
}
# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=graph_header)
# print(response.text)


# actual graph: https://pixe.la/v1/users/jessie16/graphs/graph1

# https://pixe.la/v1/users/a-know/graphs/test-graph
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
# {"message":"Success.","isSuccess":true}
pixela_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# https://www.w3schools.com/python/python_datetime.asp
today = datetime.now().strftime("%Y%m%d")
# update a random day
# random_day = datetime(year=2021, month= 7, day=23).strftime("%Y%m%d")
value_params = {
    "date": today,
    "quantity": "30"
}
# response = requests.post(url=pixela_value_endpoint, json=value_params, headers= graph_header)
# print(response.text)

# put = update requests
# $ curl -X PUT https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"name":"graph-name","unit":"commit","color":"shibafu","timezone":"Asia/Tokyo","purgeCacheURLs":["https://camo.githubusercontent.com/xxx/xxxx"],"publishOptionalData":true}'
# {"message":"Success.","isSuccess":true}
pixela_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_values_params = {
    "quantity": "50",
}
response = requests.put(url=pixela_pixel_endpoint, json=update_values_params, headers= graph_header)
print(response.text)

# delete requests
# response_delete = requests.put(url=pixela_pixel_endpoint, headers=graph_header)
