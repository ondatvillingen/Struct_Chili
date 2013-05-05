import smtplib



FROM = "*" # add sender email adress
TO = ["tweet@tweetymail.com"] # must be a list

username = '*' #add username
password = '*' #add password 

SUBJECT = "This"

TEXT = "is the third test, i'm getting thirsty!"

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail


server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(FROM, TO, message)
server.quit()
print "it's sent to %s" % (TO)