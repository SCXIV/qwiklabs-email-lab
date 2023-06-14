#!/usr/bin/env python3

import os
import os.path
from email.message import EmailMessage


message = EmailMessage()
sender = "testscript@example.com"
recipient = os.environ['GMAIL']

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Testing email sending script. Sent from {}'.format(sender)
body = "Body message of email. Sent from python script on local Linux machine"
message.set_content(body)

print(message)
