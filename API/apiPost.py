import requests
import json


def post_balance(data):
    # API request URL
    url = "http://145.24.222.140:8080/api/balance"
    headers = {"Content-type": "application/json"}

    # Send the POST request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Return the API response in JSON format
    return response


def post_withdraw(data):
    # API request URL
    url = "http://145.24.222.140:8080/api/withdraw"
    headers = {"Content-type": "application/json"}

    # Send the POST request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Return the API response in JSON format
    return response
