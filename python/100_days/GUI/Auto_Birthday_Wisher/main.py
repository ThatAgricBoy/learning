import smtplib
from email.mime.text import MIMEText

subject = "Python MailDrop"
body = """
Hello Dev.
This is still a test
Like I said it just a test
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
