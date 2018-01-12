

# python send the email via gmail account 
# please set the security level of sending gmail accout first 
# https://www.google.com/settings/security/lesssecureapps
# ref http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python


def send_email(user, pwd, recipient, subject, body):
   import smtplib

   gmail_user = user
   gmail_pwd = pwd
   FROM = user
   TO = recipient if type(recipient) is list else [recipient]
   SUBJECT = subject
   TEXT = body

   # Prepare actual message
   message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
   """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:
       server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
       server_ssl.ehlo() # optional, called by login()
       server_ssl.login(gmail_user, gmail_pwd)
       server_ssl.sendmail(FROM, TO, message)
       server_ssl.close()
       print ('successfully sent the mail')
   except:
       print ("failed to send mail")
