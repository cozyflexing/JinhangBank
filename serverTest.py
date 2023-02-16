import requests

l = requests.get("https://145.24.222.82:8080")
print(l.text)
