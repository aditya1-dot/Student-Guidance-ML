import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ranking import rank

def send_email(subject, body, to_email):
    # Replace with your email and password
    sender_email = "venkateshsanwal@gmail.com"
    password = "ohbj xphw dkix dlez"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body to the message
    message.attach(MIMEText(body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Log in to the email account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())
        print("sent")

