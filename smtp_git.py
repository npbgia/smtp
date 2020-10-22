#smtp
#Using Python library smtplib send email by Gmail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Login Gmail
def login_gmail(gmail_user,gmail_password ):
    try:
         server = smtplib.SMTP(host ='smtp.gmail.com', port = 587)
         server.ehlo()
         server.starttls()
         server.login(gmail_user, gmail_password)
         print('Login email %s successfull'%gmail_user)
         return server
    except:
         print('Something went wrong...')

#Send Email
def send_mail(subject,from_email, to_emails,  bcc_emails, login_email, login_password):
    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    #msg['Cc'] = ", ".join(cc_emails)
    msg['Bcc'] = ", ".join(bcc_emails)
    msg['Subject'] = subject
    content = 'Noi dung email'
    # if html != None:
    #     html_part = result
    #     msg.attach(html_part)
    msg.attach(MIMEText(content, 'plain'))
    msg_str =msg.as_string()
    send_to_list = to_emails + bcc_emails
    # login to my smtp server
    server = login_gmail(login_email,login_password)
    server.sendmail( from_email, send_to_list, msg_str)
    server.quit()

gmail_user = 'your_email@gmail.com'
gmail_password = 'your_email_password'

send_mail(subject = 'Test Email Subject',from_email = 'Email From Title',to_emails = ['to_email@gmail.com'] ,bcc_emails=['bcc_email1@gmail.com','bcc_email2@gmail.com'], login_email=gmail_user, login_password=gmail_password)