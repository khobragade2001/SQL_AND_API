import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    data = requests.get(url).json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        password = user_data["login"]["password"]
        country = user_data["location"]["country"]
        return username, country, password

    else:
        raise Exception("Fail to fetch method .....")

user, coun, passw = fetch_random_user()
print("user name : ", user)
print("country name : ", coun)
print("password : ",passw)
