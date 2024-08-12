import requests

def post_request():
    url = "https://reqres.in/api/users/2"
    data = {
            "id":"01",
            "email":"khobragade2001@gmail.com",
           "first_name" : "Ashish",
           "last_name" : "khobragade",
           "password" : "Ashish@003"
                }
    responce = requests.post(url, json=data)
    status_code = responce.status_code

    if (status_code == 201):
       print("status code :", status_code)
       print("Indicates that the POST request was successful, and a new resource was created as a result. ")

    elif (responce.status_code == 409):
        print("status code :", status_code)
        print(" Above status code indicate data already present in server........")

    elif(status_code == 400):
        print("status code :", status_code)
        print("Indicates that the server could not understand the request due to invalid syntax,")
    else:
        assert False


    print("responce body :",responce.json())

## callling of functions
post_request()