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
    to = []

    with open("recipients.txt", "r") as f:
        for line in f:
            email = line.strip()
            to.append(email)

    body = random_quotes
    subject = 'Dev Samurai Monday Motivation'

    for recipient in to:
        email_text = f"""\
From: {sent_from}
To: {recipient}
Subject: {subject}
{body}
"""
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(sent_from, recipient, email_text)
            server.close()

            print(f'Email sent to {recipient}!')
        except smtplib.SMTPException as e:
            print(f'Error sending email to {recipient}: {str(e)}')
else:
    print('Today is not Monday, no emails sent.')
