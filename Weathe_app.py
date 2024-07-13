import requests

api_key ='a6a8b2894aa0924aa4150dc42ba3f326'

user_input = input("Enter the city: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#if print(response.status_code) outputs to 200, the it means the request was succesful.

if (response.json()['cod'] == '404'):
#'cod' is the status code that the api returns.
    print("City does not exist")
else:
    Weather = response.json()['weather'][0]['main']
    Temp = round(((response.json()['main']['temp'])-30)/2)

    print(f"Weather in {user_input}: {Weather}")
    print(f"Temperature in {user_input}: {Temp}°C")
    #To get the degree symbol alt+0176.
