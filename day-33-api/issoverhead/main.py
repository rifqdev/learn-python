import requests
from datetime import datetime, timedelta
import smtplib
import time

MY_EMAIL = "sample@gmail.com"
MY_PASS = "sampleepass"

MY_LAT = -7.575830
MY_LONG = 108.765120 

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    utc_sunrise = datetime.fromisoformat(data["results"]["sunrise"])
    utc_sunset = datetime.fromisoformat(data["results"]["sunset"])
    wib_sunrise = utc_sunrise + timedelta(hours=7)
    wib_sunset = utc_sunset + timedelta(hours=7)

    time_now = datetime.now()

    # Cek posisi ISS
    lat_range = (MY_LAT - 5.0) <= iss_latitude <= (MY_LAT + 5.0)
    lon_range = (MY_LONG - 5.0) <= iss_longitude <= (MY_LONG + 5.0)

    # Cek waktu 
    is_dark = time_now.hour >= wib_sunset.hour or time_now.hour <= wib_sunrise.hour
    
    if lat_range and lon_range and is_dark:
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASS)
                connection.sendmail(
                    MY_EMAIL, 
                    MY_EMAIL, 
                    "Subject:LOOK UP👆\n\n The ISS is above you in the sky.\n\n Posisi ISS: {iss_latitude}°, {iss_longitude}°"
                )
            print("Email terkirim!")
        except Exception as e:
            print(f"Gagal mengirim email: {e}")
    
    time.sleep(60)