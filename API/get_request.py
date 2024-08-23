import json

import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    data = requests.get(url).json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        password = user_data["login"]["password"]
        country = user_data["location"]["country"]
        return username, country, password, data

    else:
        raise Exception("Fail to fetch method .....")

user, coun, passw,data = fetch_random_user()
print("user name : ", user)
print("country name : ", coun)
print("password : ",passw)
print("status code :")
pritty = json.dumps(data, indent=5)
print(pritty)
