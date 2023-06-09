import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = 'devsamurai4@gmail.com'
MY_PASSWORD = 'yhygoimvgfzfeysg'

dates = dt.datetime.now()
today = (dates.month, dates.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for _, data_row in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read().replace("[NAME]", birthday_person["name"])

    sent_from = MY_EMAIL
    to = [birthday_person["email"]]
    subject = 'Happy Birthday'
    body = contents

    email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}

{body}
"""

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(sent_from, to, email_text)

        print('Email sent!')
    except smtplib.SMTPException as e:
        print(f'Error sending email: {str(e)}')
else:
    print('No birthdays today.')
