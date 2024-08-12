import requests

def Patch_request():
    url = "https://api.freeapi.app/api/v1/social-media/profile"
    data = {"name":"ashish"}
    responce = requests.patch(url,data)
    # user_data = data["data"]["coverImage"]["firstName":"Ashish khobragade"]


    print(responce.headers)
    print(responce.status_code)

## calling
Patch_request()