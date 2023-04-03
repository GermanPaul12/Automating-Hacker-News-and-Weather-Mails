import requests
import yagmail
from .. import secret
from send_mail import send_email

def rain_checker():
    #Leimen
    weather_parameters = {
        "lat":secret.MY_LAT,
        "lon":secret.MY_LNG,
        "appid":secret.WEATHER_API_KEY,
        "exclude":"current,minutely,daily"
    }

    url = "https://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(url, params=weather_parameters)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False

    for index in range(14):
        weather_main = weather_data["hourly"][index]["weather"][0]["id"]
        if weather_main < 700:
            will_rain = True

    if will_rain:
        send_email(secret.ANGI_EMAIL, "Wetterbericht für Leimen! von German Paul☔️️", "Hey Angi,\n\nEs wird heute in Leimen regnen, daher solltest du einen Regenschirm mitnehmen!\n\nLiebe Grüße\nGermi💌")
        send_email(secret.PERSONAL_EMAIL, "Wetterbericht für Leimen! von German Paul☔️️", "Hey German,\n\nEs wird heute in Leimen regnen, daher solltest du einen Regenschirm mitnehmen!\n\nLiebe Grüße\nGerman💌")
        send_email(secret.MAMA_EMAIL, "Wetterbericht für Leimen! von German Paul☔️️", "Hey Mama,\n\nEs wird heute in Leimen regnen, daher solltest du einen Regenschirm mitnehmen!\n\nLiebe Grüße\nGerman💌")
    #Mannheim
    weather_parameters = {
        "lat":secret.MA_LAT,
        "lon":secret.MA_LNG,
        "appid":secret.WEATHER_API_KEY,
        "exclude":"current,minutely,daily"
    }

    url = "https://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(url, params=weather_parameters)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False

    for index in range(14):
        weather_main = weather_data["hourly"][index]["weather"][0]["id"]
        if weather_main < 700:
            will_rain = True

    if will_rain:
        send_email(secret.PERSONAL_EMAIL, "Wetterbericht für Mannheim! von German Paul☔️️", "Hey German,\n\nEs wird heute in Mannheim regnen, daher solltest du einen Regenschirm mitnehmen!\n\nLiebe Grüße\nGerman💌")

if __name__ == "__main__":
    rain_checker()