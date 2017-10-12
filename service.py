import commands
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#find process
pc = commands.getoutput('ps -aux | grep apache2 | grep -v grep')
#pc returns the process id number
#if service running it will print otherwise it returns a 0
if(len(pc) > 0):       
	print "service is running"
else:
        fromaddr = "sandeep.click7@gmail.com"
        toaddr = "sandeep@5gindia.net"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "SERVICE STATUS"

        body = "Apache service is not running"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "Amma@1994")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


