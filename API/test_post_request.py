import requests

def post_request():
    url = "https://api.freeapi.app/api/v1/users/register"
    data = {
           "email" : "vijay.setupati@outlook.com",
           "username" : "vijaysetupati",
           "password" : "Vijay@003"
    }
    responce = requests.post(url, json=data)

    if (responce.status_code == 201):
       assert True
    elif (responce.status_code == 409):
        print("data already present in server........")
    else:
        assert False

    print("status code :",responce.status_code)
    print("responce body :",responce.json())

## callling of functions
post_request()