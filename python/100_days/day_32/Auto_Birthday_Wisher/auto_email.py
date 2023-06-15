from random import choice
import datetime as dt
import smtplib

MY_EMAIL = "devsamurai4@gmail.com"
MY_PASSWORD = "yhygoimvgfzfeysg"

date = dt.datetime.now()
today = date.weekday()
if today == 0:
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        random_quotes = choice(quotes)

    sent_from = MY_EMAIL
    to = ['samueljohn3999@gmail.com']
    body = random_quotes
    subject = 'Dev Samurai Monday Motivations'

    email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}
{body}
"""

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except smtplib.SMTPException as e:
        print(f'Error sending email: {str(e)}')
