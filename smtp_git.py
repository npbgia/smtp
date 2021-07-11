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
    server.sendmail(from_email, send_to_list, msg_str)
    server.quit()

gmail_user = 'emailcuatui@gmail.com'
gmail_password = 'passwordcuatui'

#login_gmail(gmail_user,gmail_password)
send_mail(subject = 'Test Khai giang khoa hoc',
          from_email = 'Email From Title',
          to_emails = ['toemail@gmail.com'] ,
          bcc_emails=['bccemail@gmail.com'],
          login_email=gmail_user,
          login_password=gmail_password)