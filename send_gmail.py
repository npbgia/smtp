#smtp
#Using Python library smtplib send email by Gmail

import smtplib
from string import Template
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
    except Exception as E:
         print('Something went wrong...', E)

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        line = contacts_file.read().split('\n')
        for a_contact in line:
            names.append(a_contact.split(',')[0])
            emails.append(a_contact.split(',')[1])
            # print(names)
            # print(emails)
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        # print(template_file_content)
    return Template(template_file_content)

#Send Email
def send_mail(subject, login_email, login_password): # subject,from_email, login_email, login_password
    names, emails = get_contacts(r'D:\01.myWorking\myGit\smtp\email_list.txt')  # read contacts
    message_template = read_template(r'D:\01.myWorking\myGit\smtp\email_content.txt')

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        # print(message)

        print('name:',name,'email:',email)
        bcc_names = []
        bcc_emails = []
        bcc_names.append(name)
        bcc_emails.append(email)
        #print(bcc_emails)
        #assert isinstance(to_emails,list)
        msg = MIMEMultipart('alternative')
        msg['From'] = login_email
        #msg['To'] = ", ".join(to_emails)
        #msg['Cc'] = ", ".join(cc_emails)
        msg['Bcc'] = email
        #print(email)
        msg['Subject'] = subject
        content = message
        # if html != None:
        #     html_part = result
        #     msg.attach(html_part)
        msg.attach(MIMEText(content, 'plain'))
        msg_str =msg.as_string()
        send_to_list = bcc_emails # to_emails +
        # login to my smtp server
        server = login_gmail(login_email,login_password)
        server.sendmail(login_email, send_to_list, msg_str)
        server.quit()

gmail_user = 'emailcuatui@gmail.com'
gmail_password = 'passwordcuatui'

send_mail(subject = 'Tieu de email',
          login_email=gmail_user,
          login_password=gmail_password
          )