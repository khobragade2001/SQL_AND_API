import requests

def delete_request():
    url = "https://reqres.in/api/users/3"
    data = {"first_name":"Ashish"}

    responce = requests.delete(url, json=data)
    status_code = responce.status_code

    if ( status_code== 200):
        print("status code :",status_code)
        print("Indicates that the DELETE request was successful, "
             "and the server is returning a response body, "
             "which may include information about the deleted resource")

    elif (status_code == 202):
        print("status code :", status_code)
        print(" Indicates that the DELETE request has been accepted for processing, "
              "but the processing has not been completed. This is typically used for asynchronous operations.")

    elif (status_code == 204):
        print("status code :", status_code)
        print("Indicates that the DELETE request was successful, "
              "but the server is not returning any content in the response body. "
              "The resource was successfully deleted.")

    elif (responce.status_code == 401):
        print("status code :", status_code)
        print("Unauthorized.....")

    else:
        assert False




    ## callling of functions
delete_request()