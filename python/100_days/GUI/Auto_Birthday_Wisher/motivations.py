import smtplib

gmail_user = 'devsamurai4@gmail.com'
gmail_password = 'yhygoimvgfzfeysg'

sent_from = gmail_user
to = ['samueljohnmaxi@gmail.com']
subject = 'Dev Samurai Monday Motivations'
body = 'Hey, You will be fine'

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
