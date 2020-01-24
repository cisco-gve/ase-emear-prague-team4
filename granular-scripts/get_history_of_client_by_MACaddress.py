import requests

url = "https://msesandbox.cisco.com:8081/api/location/v1/history/clients/"

headers = {
    'authorization': "xxxxxxxxx",
    'cache-control': "no-cache",
    'postman-token': "xxxxxxxxx"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
