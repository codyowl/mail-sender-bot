import smtplib

USER_NAME = "your username" 

PASSWORD = "your password"

EMAIL_BOT_COUNT = raw_input("How many email bots you want to create: ")

FROM = "from@gmail.com"

TO = "to@live.com"

Cc = ["ccs@gmail.com"]


def email_bot_creator(email_bot_count):
    for i in range(len(email_bot_count)):
        print "Enter details for bot no: %s" % (i + 1)
        to = raw_input("Enter the To address: ")
        cc_checker = raw_input("Do you want to add cc ?(y/n): ")
        if cc_checker.lower() == 'y':
            cc = raw_input("Enter the Cc address: ")
        subject = raw_input("Enter the Subject: ")
        content = raw_input("Enter the content: ")
        time = raw_input("At what time you want to shoot this mail(mention like this hh:mm with am and pm): ")
        time_processor_method = time_processor(time)
        hours = time_processor_method[0]
        minutes = time_processor_method[1]
        meridiem = time_processor_method[2]
        railway_time_converter_method = railway_time_converter(hours, minutes, meridiem)
        print railway_time_converter_method
        
def railway_time_converter(hours, minutes, meridiem):
    if meridiem == 'pm':
        hours = int(hours) + 12
        time = '%s:%s' % (hours, minutes)
    else:
        time = '%s:%s' % (hours, time)
    return time  
    
def time_processor(time):
    time_splitter = time.split(':')
    meridiem_splitter = time_splitter[1].split(' ')
    hours = time_splitter[0]
    minutes = meridiem_splitter[0]
    meridiem = meridiem_splitter[1]
    return hours, minutes, meridiem



# message = "From: %s\r\n" % FROM + "To: %s\r\n" % TO + "CC: %s\r\n" % ",".join(Cc)+ "Subject: %s\r\n" % SUBJECT + "\r\n" + CONTENT

# receivers = [TO] + Cc        

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
    

email_bot_creator(EMAIL_BOT_COUNT)
# mail_sender(USER_NAME, PASSWORD, FROM, receivers, message)
