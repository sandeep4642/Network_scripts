import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime

hostname = ['5gautomatika.com','5genergy.ca','5genergy.org','5gindia.com','5gindia.in','drgsundaram.com','ec4energy.co.uk','ec4energy.com','enterprise-gateway.com','fifthgentech.com','itsme.org.in','payit.5genergy.ca','payit.5gindia.com','staging.5gindia.com','support.5gindia.com']
now=datetime.datetime.now()
#and then check the response...
for nw in hostname:
        response = os.system("ping -c 6 " + nw)
        if response != 0:
                fromaddr = "sandeep.click7@gmail.com"
                recipients = 'sandeep@5gindia.net,sundar@fifthgentech.com'

                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = recipients

                msg['Subject'] = "DOMAIN DOWN"

                body = "%r IS DOWN AT" % nw + " " + now.strftime("%Y-%m-%d %H:%M")

                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(fromaddr, "Amma@1994")
                text = msg.as_string()
                server.sendmail(fromaddr, recipients.split(','), text)
                server.quit()



