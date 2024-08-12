import requests

def delete_request():
    url = "https://api.freeapi.app/api/v1/chat-app/chats/group/64ca9e166cabe93cce077e0a"

    responce = requests.delete(url)

    if (responce.status_code == 200):
       assert True
    elif (responce.status_code == 401):
        print("Unauthorized request........")
    else:
        assert False

    print("status code :", responce.status_code)
    print("responce body :", responce.json())

    ## callling of functions
delete_request()