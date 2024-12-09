import requests

API_KEY = 'ваш_api_ключ'
CITY = 'Ulyanovsk'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather = data['main']
        temperature = weather['temp']
        pressure = weather['pressure']
        humidity = weather['humidity']
        print(f'Погода в {CITY}: {temperature}°C, Давление: {pressure} гПа, Влажность: {humidity}%')
    else:
        print(f'Ошибка: {response.status_code}')

get_weather()
