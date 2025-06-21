import requests

url = "http://127.0.0.1:8000/query"
payload = {"question": "Show all products"}

response = requests.post(url, json=payload)
print(response.json())
