
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime

hostname = ['192.168.1.1','192.168.1.3','192.168.1.102','192.168.1.13','192.168.1.98'] #list of ip's
now=datetime.datetime.now()
#and then check the response...
for nw in hostname:
        response = os.system("ping -c 1 " + nw)
        if response != 0:
                fromaddr = "sandeep.click7@gmail.com"
                toaddr = "sandeep@5gindia.net"

                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr

                msg['Subject'] = "NETWORK DOWN"

                body = "%r IS DOWN AT" % nw + " " + now.strftime("%Y-%m-%d %H:%M")

                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(fromaddr, "Amma@1994")
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()

