from flask_mail import Message
from app import mail
from flask import current_app

def send_contact_email(name, email, subject, message):
    """Send an email to the site administrator with the contact form details."""
    msg = Message(
        subject=f"Contact Form Submission: {subject}",
        sender = (current_app.config['MAIL_USERNAME'], current_app.config['MAIL_DEFAULT_SENDER']),
        recipients = ["mccluskeylucy30@gmail.com"]
    )
    msg.body = f"""
    Name: {name}
    Email: {email}
    Subject: {subject}
    Message: {message}
    """
    mail.send(msg)