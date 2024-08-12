import requests

def Put_request():
    url = "https://reqres.in/api/users/2"  # Assuming you are updating user with ID 2
    data = {
        "id": "01",
        "first_name": "Ashish Khobragade",
        "last_name":"khobragade"
                }

    response = requests.put(url, json=data)  # Use json parameter for sending JSON data
    status_code = response.status_code


    if (status_code == 200):
        print("status code :",status_code)
        print("This status code means the PUT request was successful, "
              "and the server is returning the updated resource in the response body..")

    elif (status_code == 201):
        print("status code :", status_code)
        print("This status code indicates that the PUT request resulted in the creation of a new resource. "
              "This happens if the resource did not exist before and was created as a result of the request.")

    elif (status_code == 202):
        print("status code :", status_code)
        print("This status code means that the request has been accepted for processing, "
              "but the processing has not been completed. "
              "This is often used in asynchronous operations.")

    elif (status_code == 204):
        print("status code :", status_code)
        print("This status code means the PUT request was successful, "
              "but the server is not returning any content in the response body. "
              "The resource was updated, but there’s nothing more to send back to the client.")
    else:
        print("status code :", status_code)
        print("Request failed.")

    print(response.json())  # Print the JSON response to understand the result
    print(response.headers)
    print(response.url)


# Calling the method
Put_request()


