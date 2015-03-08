import smtplib
from email import encoders 
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from django.conf import settings


def sendmail(destination,subject="Subject 0",html="",f=None):
	import smtplib
	import os
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	smtp = smtplib.SMTP('smtp.gmail.com:587')
	smtp.set_debuglevel(False)
	smtp.ehlo()
	smtp.starttls()
	smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)

	sender=settings.EMAIL_USER

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['Cci'] = ", ".join(destination)

	# Create the body of the message (a plain-text and an HTML version).
	text = "" # I don't know what this might be for (???)

	if f :
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(f, 'rb').read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment; filename="%s"' % basename(f))
		msg.attach(part)


	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	
	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	smtp.sendmail(sender, destination, msg.as_string())
