import smtplib
from email.mime.text import MIMEText
import os

class NotificationManager:
    def __init__(self):
        self.subject = "Cheap Flight Alert"
        self.body = """
        You can now book your flight. 
        The price is exactly where you want it.
        """
        self.sender = "samueljohnmaxi@gmail.com"
        self.recipients = ["samueljohn3999@gmail.com"]
        self.password = os.environ.get("GMAIL")

    def send_email(self, body):
        msg = MIMEText(body)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, self.recipients, msg.as_string())
        print("Message sent!")
