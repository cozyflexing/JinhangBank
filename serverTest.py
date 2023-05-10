import requests, json

url = "http://145.24.222.16:8000/api/data"
response = requests.get(url)

if response.status_code == 200:
    raw_data = response.json()
    print("API response:", raw_data)
else:
    print("Error:", response.status_code, response.text)

# Convert the list data into dictionaries
data = {}

data["adressen"] = [
    {"id": addr[0], "street_number": addr[1], "postal_code": addr[2]}
    for addr in raw_data["adressen"]
]

data["klanten"] = [
    {
        "id": klant[0],
        "first_name": klant[1],
        "middle_name": klant[2],
        "last_name": klant[3],
        "email": klant[4],
        "phone": klant[5],
        "birthdate": klant[6],
        "address_id": klant[7],
    }
    for klant in raw_data["klanten"]
]

data["bankpassen"] = [
    {
        "id": pas[0],
        "card_number": pas[1],
        "pin": pas[2],
        "blocked": bool(pas[3]),
        "account_number": pas[4],
        "customer_id": pas[5],
    }
    for pas in raw_data["bankpassen"]
]

data["rekeningen"] = [
    {"account_number": rek[0], "balance": rek[1]} for rek in raw_data["rekeningen"]
]

data["transacties"] = [
    {
        "id": trans[0],
        "date": trans[1],
        "time": trans[2],
        "description": trans[3],
        "type": trans[4],
        "amount": trans[5],
        "card_id": trans[6],
        "account_number": trans[7],
    }
    for trans in raw_data["transacties"]
]

with open("bankdata.json", "w") as file:
    json.dump(data, file, indent=2)
