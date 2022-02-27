import requests
from twilio.rest import Client


# Twilio credentials
SID = "AC6ca448808272c59bd8cdbf0d8c367c52"
AUTH_TOKEN = "b32f8209cd7d73b0b29426a2d13cf0c7"
MY_Number = "+18646354721"


api_key = "d57940cdeb3d2e34641eafbe0e3598ea"
# lat = "-17.821643"
# lon = "31.113743"

lat = -27.079
lon = 28.938

url = "https://api.openweathermap.org/data/2.5/weather?lat=-17.821643&lon=31.113743&appid=d57940cdeb3d2e34641eafbe0e3598ea"

url2 = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily,alerts&appid={api_key}"

params = {
    "lat:": lat,
    "lon": lon,
    "appid": api_key,
}


response = requests.get(url2)
response.raise_for_status()

will_rain = False

data = response.json()['hourly']
for i in range(12):
    if data[i]["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    client = Client(SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain, bring an umbrella",
            from_=MY_Number,
            to='+263773587559'
        )

    print(message.status)
