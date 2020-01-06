import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def text(str):
    email = os.environ.get('GMAIL_EMAIL')
    pas = os.environ.get('GMAIL_PASS')
    phone = os.environ.get('PHONE_NUMBER')
    provider = os.environ.get('PROVIDER')
    sms_gateway = '%s@txt.%s' % (phone, provider)
    smtp = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,pas)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "craigslist listing\n"
    body = "%s" % (str) + '\n'
    msg.attach(MIMEText(body, 'html'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)
