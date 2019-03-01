import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''from_gmail_user = 'scoutbotsem4@gmail.com'
from_gmail_password = 'scoutbot@123'''
from_gmail_user = 'mail id'
from_gmail_password = 'password'
user = '#receiver mail id'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_gmail_user, from_gmail_password)
print("logged in")
# ...send emails
i=0
while(True):
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "loop-" + str(i+1)
	body = "Hello !"
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	i +=1
	if(i==1):
		break
server.quit()
#print("Something went wrong...")
