import requests

r = requests.get("http://192.168.100.123:8080/")
print(r.json())