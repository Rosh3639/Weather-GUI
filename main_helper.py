import pyowm
from datetime import datetime
from api import API_KEY

# Add your own API_KEY from OpenWeather.com
owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Nashik, India', '3h')
forecast = forecaster.forecast


def get_temperature():
    days = []
    dates = []
    temp_min = []
    temp_max = []
    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature('celsius')['temp']
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    print(days, temp_min, temp_max)
    return days, temp_min, temp_max


if __name__ == '__main__':
    get_temperature()
