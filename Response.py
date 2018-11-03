from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib

#Establish variables for sender
sender = "cyberchau@gmail.com"
username = "edchau"
password = CyberReborn
host = "smtp.myserver.com"
port = 587

#Prompt for recipients email address
recipient1 = "cyberchau@gmail.com"
recipient2 = "echau@go.pasadena.edu"
body = "HELLO"
subjectLine = "HELLO HUMAN"

#Create a message
msg = MIMEMultipart()

##Specify email address of sender and recipients
#Sender
msg["From"] = sender
#Reciever(s)
msg["To"] = recipient1
msg["Bcc"] = recipient2

#Set Subject line
msg["Subject"] = subjectLine

#Attach message body as plain text
msg.attach(MIMEText(body, "plain"))

#Connect to gmail server
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host, port)

#Turn on secure communications, log in to server, and quit
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()
