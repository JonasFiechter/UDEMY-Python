from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='John', data=data)

print(corpo_msg)