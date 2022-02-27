import requests
import datetime as dt

LAT = -17.805160
LON = 31.125110


def is_overheard():
    iss = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=iss)
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if longitude + LON <= 5 and latitude + LAT <= 5 and longitude - LON >= -5 and latitude - LAT >= -5:
        return True


if is_overheard():
    print("Overheard")
else:
    print("Not Overheard")

parameters = {"lat": "-17.805160", "lon": "31.125110", "formatted": 0}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

rise = sunrise.split("T")[1].split(":")[0]
set = sunset.split("T")[1].split(":")[0]


now = dt.datetime.now().hour

# check if its between 6pm and 6am


def is_night():
    if now >= int(set) or now <= int(rise):
        return True
    else:
        return False


if is_night() and is_overheard():
    print("Look UP")
