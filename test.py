import requests
import json

# for /api/balance
data = {"acctNo": "CHJNHB987654321", "pin": "8888"}
response = requests.post(
    "http://145.24.222.16:8080/api/balance",
    data=json.dumps(data),
    headers={"Content-Type": "application/json"},
)

# for /api/withdraw
data = {"acctNo": "CHJNHB987654321", "pin": "5588", "amount": 500}
response = requests.post(
    "http://145.24.222.16:8080/api/withdraw",
    data=json.dumps(data),
    headers={"Content-Type": "application/json"},
)
