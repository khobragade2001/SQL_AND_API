import requests

def Patch_request():
    url = "https://reqres.in/api/users/2"
    data = {"first_name":"ashish","last_name":"Khobragade","text":"update at 12 aug"}
    responce = requests.patch(url, json=data)

    status_code = responce.status_code

    if (status_code == 200):
        print("status code :",responce.status_code)
        print("This status code means that the PATCH request was successful, "
              "and the server is returning the updated resource in the response body.")
    elif (status_code == 204):
        print("status code", responce.status_code)
        print("This status code indicates that the PATCH request was successful, "
              "but the server is not returning any content in the response body.")
    elif (status_code == 202):
        print("status code", responce.status_code)
        print("This status code means that the request has been accepted for processing, "
              "but the processing has not been completed.")
    else:
        assert False

    print(responce.json())
## calling
Patch_request()