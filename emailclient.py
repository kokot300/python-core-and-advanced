import smtplib
from email.mime.text import MIMEText

body="hello world"
msg=MIMEText(body)
msg['From']="poesiaco@gmail.com"
msg['To']="kokot300@gmail.com"
msg['Subject']="Hello!!!"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("poesiaco@gmail.com","13061990")
server.send_message(msg)
print("email sent!")
server.quit()