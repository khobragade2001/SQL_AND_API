import requests


def Put_request():
    url = "https://api.freeapi.app/api/v1/seed/ecommerce"
    # data = {data :"Ashish Khobragade"}

    responce  = requests.put(url, data="Ashish")
    print(responce)
    print(responce.headers)
    print(responce.url)
    status = (responce.status_code)
    
    if (status == 200):
        assert True
    else:
        assert False


## calling of method
Put_request()

