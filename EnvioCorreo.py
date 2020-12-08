from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import logging

"""
data = {}
with open('pass.json') as f:
        data = json.load(f)
"""

def Envio_Correo(user, contra, destinatario, asunto, mensaje):
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From'] =  user #data['user']
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # add in the message body
    msg.attach(MIMEText(mensaje, 'plain'))

    #create server #smtp.office365.com
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()

    # Login Credentials for sending the mail
    print(user)
    server.login(user, contra)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print("successfully sent email to %s:" % (msg['To']))
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('correo enviado correctamente.')
