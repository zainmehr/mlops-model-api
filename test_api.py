import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "size": 120,
    "nb_rooms": 3,
    "garden": 1
}

response = requests.post(url, json=data)
print(response.status_code)  # 200
print(response.json())       # {'y_pred': ...}