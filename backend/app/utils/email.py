import smtplib
import os
from email.mime.text import MIMEText


def send_otp_email(to_email: str, otp: str):
    host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    port = int(os.getenv("SMTP_PORT", "587"))
    sender = os.getenv("SMTP_FROM_EMAIL") or os.getenv("SMTP_USERNAME")
    username = os.getenv("SMTP_USERNAME") or sender
    password = os.getenv("SMTP_PASSWORD")

    if not sender or not username or not password:
        raise RuntimeError("SMTP credentials are not configured")

    msg = MIMEText(f"Your OTP code is: {otp}\n\nIt expires in 5 minutes.")
    msg["Subject"] = "Your OTP Verification Code"
    msg["From"] = sender
    msg["To"] = to_email

    if port == 465:
        with smtplib.SMTP_SSL(host, port) as server:
            server.login(username, password)
            server.sendmail(sender, to_email, msg.as_string())
    else:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, to_email, msg.as_string())