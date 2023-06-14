#!/usr/bin/env python3

import os
import os.path
import mimetypes
from email.message import EmailMessage


message = EmailMessage()

# Defines sender and recipient
sender = "testscript@example.com"
recipient = os.environ['GMAIL']

# Defining attachable path and name
attachment_path = "/image/image.jpg"
attachment_filename = os.path.basename(attachment_path)

# Using MIME to define type of file being sent
mime_type, mime_subtype = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Testing email sending script. Sent from {}'.format(sender)
body = "Body message of email. Sent from python script on local Linux machine"
message.set_content(body)

print(message)