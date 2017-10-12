import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "sandeep.click7@gmail.com"
toaddr = "sandeep@5gindia.net"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr

msg['Subject'] = "NETWORK STATUS"
body = "EVERY THING GOING GOOD" 
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Amma@1994")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

