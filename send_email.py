import smtplib, ssl
import os


def send_email(message):
    """Send an email with data"""
    host = "smtp.gmail.com"
    port = 465

    username = "adamidrissi177@gmail.com"
    password = "ammo rtym savl mxsw "

    receiver = "30443@ras.ma"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
