import smtplib
from random import choice
import datetime as dt
import smtplib

date = dt.datetime.now()
today = date.weekday()
if today == 3:
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        random_quotes = choice(quotes)

    gmail_user = 'devsamurai4@gmail.com'
    gmail_password = 'yhygoimvgfzfeysg'

    sent_from = gmail_user
    to = ['samueljohnmaxi@gmail.com']
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
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
