import smtplib

USER_NAME = "your username" 

PASSWORD = "your password"

SUBJECT = raw_input("Enter the subject :")

CONTENT = raw_input("Enter the mail content :")

EMAIL_BOT_COUNT = raw_input("How many email bots you want to create: ")

FROM = "from@gmail.com"

TO = "to@live.com"

Cc = ["ccs@gmail.com"]

def email_bot_creator(email_bot_count):
    for i in range(len(email_bot_count)):
        print "Enter details for bot no: %s" % (i)
        to = raw_input("To: ")
        subject = raw_input("Subject: ")
        content = raw_input("enter your content: ")
        time = raw_input("At what time you want to shoot this mail(mention am and pm): ")

message = "From: %s\r\n" % FROM + "To: %s\r\n" % TO + "CC: %s\r\n" % ",".join(Cc)+ "Subject: %s\r\n" % SUBJECT + "\r\n" + CONTENT

receivers = [TO] + Cc        

def mail_sender(username, password, FROM, receivers, message):
	# SECONDS = TIME * 60
    # time.sleep(float(SECONDS))

	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(FROM, receivers, message)
		server.close()
		print "mail sent !"

	except:
	   print "failed to send the mail" 
	


mail_sender(USER_NAME, PASSWORD, FROM, receivers, message)
