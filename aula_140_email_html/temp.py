from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'jonastestepython@gmail.com'
minha_senha = ''

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='John', data=data)

corpo = MIMEText(corpo_msg, 'html')

msg = MIMEMultipart()
msg['from'] = 'John Anything'
msg['to'] = meu_email
msg['subject'] = 'This is an test e-mail'
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('Email sent')