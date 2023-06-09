import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time

MY_EMAIL = "devsamurai4@gmail.com"
MY_PASSWORD = "yhygoimvgfzfeysg"
MY_LAT = 7.348720
MY_LONG = 3.879290
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude and MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now<= sunrise:
        return True
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        subject = "Geo Check"
        body = """
        Look Up!
        You are about to
        See something
        Amazing
        """
        sender = "devsamurai4@gmail.com"
        recipients = "samueljohn3999@gmail.com"
        password = "yhygoimvgfzfeysg"


        def send_email(subject, body, sender, recipients, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
            print("Message sent!")


        send_email(subject, body, sender, recipients, password)



