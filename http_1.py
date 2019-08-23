import requests

url = "http://google.com"

params = {"test":"1","n":"2"}

response = requests.post(url, data=params)

print(response.content)