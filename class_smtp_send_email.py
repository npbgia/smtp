import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class smtp_send_email():

    def get_contacts(self,filename):
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


    def read_template(self,filename):
        """
        Returns a Template object comprising the contents of the
        file specified by filename.
        """

        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
            # print(template_file_content)
        return Template(template_file_content)


    def main(self,MY_ADDRESS, PASSWORD, email_list_path, email_message_path):

        names, emails = self.get_contacts(email_list_path)  # read contacts
        message_template = self.read_template(email_message_path)

        # set up the SMTP server
        s = smtplib.SMTP(host ='smtp-mail.outlook.com', port = 587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()  # create a message

            # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name.title())

            # Prints out the message body for our sake
            print(message)

            # setup the parameters of the message
            msg['From'] = MY_ADDRESS
            msg['To'] = email
            msg['Subject'] = "This is subject"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            s.send_message(msg)
            del msg

        # Terminate the SMTP session and close the connection
        s.quit()


if __name__ == '__main__':
    smtp = smtp_send_email()
    smtp.main()