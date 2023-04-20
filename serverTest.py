import requests, json

url = "http://145.24.222.16:8000/api/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API response:", data)
else:
    print("Error:", response.status_code, response.text)

with open("bankdata.json", "w") as file:
    json.dump(data, file, indent=2)
