import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email import encoders

sender = 'dodsas87@gmail.com'
receiver = 'dods87@naver.com'
smtpserver = 'smtp.gmail.com'
port = 587
username = 'dodsas87@gmail.com'

# import password value from config.py
from config import mailPassword
password = mailPassword

def sendMail(subject:str, text:str = "내용 없음"):
    msg = MIMEText(text)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    smtp = smtplib.SMTP(smtpserver, port)
    # smtp.set_debuglevel(1)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()