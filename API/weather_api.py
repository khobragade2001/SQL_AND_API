import json
import requests

def Weather_info():
    city_name = input("Enter City :")
    api_key = 'f33b1b3b2e4417261d161b347f6b294a'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=en&appid={api_key}&units=metric'

    responce = requests.get(url).json()


    # to get pritty data
    pritty_data = json.dumps(responce, indent=4)
    print(pritty_data)

    # we want specific information like temp, speed, humidity, status code
    if "name" in responce:
        temp = responce["main"]["temp"]
        humidity = responce["main"]["humidity"]
        max_temp = responce["main"]["temp_max"]
        min_temp = responce["main"]["temp_min"]
        speed = responce["wind"]["speed"]
        weather = responce["weather"][0]["description"]
        city_name = responce["name"]
        status_code = responce["cod"]

        print("City name is :", city_name)
        print("Status Code :", status_code)
        print("Avg Temp is :", temp)
        print("Weather Conditions :", weather)
        print("Maximum Temp :", max_temp)
        print("Minimum Temp :", min_temp)
        print("Speed of Wind :", speed)
        print("Humidity :", humidity)
    else:
        print("You are Entered Wrong City .............")


## calling of function
Weather_info()
