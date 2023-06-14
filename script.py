#!/usr/bin/env python3

import os
import os.path
import mimetypes
import smtplib
from email.message import EmailMessage

message = EmailMessage()

# Defines sender and recipient
sender = "testscript@example.com"
recipient = os.environ['GMAIL']

# Defining attachable path and name
attachment_path = "image/image.jpg"
attachment_filename = os.path.basename(attachment_path)

# Using MIME to define type of file being sent
mime_type, mime_subtype = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

# Logging into SMTP with Gmail w/ env vars
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_pass = os.environ['GMAIL_PASS']
mail_server.login(recipient, mail_pass)

# The code below creates the email
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Testing email sending script. Sent from {}'.format(sender)
body = "Body message of email. Sent from python script on local Linux machine"
message.set_content(body)

# The code below attaches the picture to the email
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# print(message)

mail_server.send_message(message)
mail_server.quit()