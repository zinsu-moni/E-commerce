import os
import smtplib
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "templates" / "emails"


def _send_message(message, sender: str, recipient: str):
    host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    port = int(os.getenv("SMTP_PORT", "587"))
    username = os.getenv("SMTP_USERNAME") or sender
    password = os.getenv("SMTP_PASSWORD")

    if port == 465:
        with smtplib.SMTP_SSL(host, port) as server:
            server.login(username, password)
            server.sendmail(sender, recipient, message.as_string())
    else:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, recipient, message.as_string())


def _render_template(template_name: str, **context) -> str:
    template_path = TEMPLATE_DIR / template_name
    raw_template = template_path.read_text(encoding="utf-8")
    return Template(raw_template).safe_substitute(**context)


def _build_message(subject: str, sender: str, recipient: str, text_body: str, html_body: str):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.attach(MIMEText(text_body, "plain", "utf-8"))
    message.attach(MIMEText(html_body, "html", "utf-8"))
    return message


def send_otp_email(to_email: str, otp: str):
    sender = os.getenv("SMTP_FROM_EMAIL") or os.getenv("SMTP_USERNAME")

    if not sender or not os.getenv("SMTP_USERNAME") or not os.getenv("SMTP_PASSWORD"):
        raise RuntimeError("SMTP credentials are not configured")

    expires_in_minutes = os.getenv("OTP_EXPIRE_MINUTES", "10")
    otp_code = str(otp)
    html_body = _render_template(
        "otp_email.html",
        expires_in_minutes=expires_in_minutes,
        otp_code=otp_code,
    )
    text_body = f"Your OTP code is: {otp}\n\nIt expires in {expires_in_minutes} minutes."
    msg = _build_message("Your OTP Verification Code", sender, to_email, text_body, html_body)

    _send_message(msg, sender, to_email)


def welcome_message(to_email: str):
    sender = os.getenv("SMTP_FROM_EMAIL") or os.getenv("SMTP_USERNAME")
    
    if not sender or not os.getenv("SMTP_USERNAME") or not os.getenv("SMTP_PASSWORD"):
        raise RuntimeError("SMTP credentials are not configured")
    
    html_body = _render_template("welcome_email.html")
    text_body = "Welcome to our service!"
    msg = _build_message("Welcome to Our Service", sender, to_email, text_body, html_body)

    _send_message(msg, sender, to_email)

def send_password_reset_email(to_email: str, reset_link: str):
    sender = os.getenv("SMTP_FROM_EMAIL") or os.getenv("SMTP_USERNAME")


    if not sender or not os.getenv("SMTP_USERNAME") or not os.getenv("SMTP_PASSWORD"):
        raise RuntimeError("SMTP credentials are not configured")

    html_body = _render_template("forgot_password_email_compatible.html", reset_link=reset_link)
    text_body = f"Reset your password here: {reset_link}\n\nThis link expires in 24 hours."
    msg = _build_message("Password Reset Request", sender, to_email, text_body, html_body)

    _send_message(msg, sender, to_email)


def password_changed_successfully(to_email: str):
    sender = os.getenv("SMTP_FROM_EMAIL") or os.getenv("SMTP_USERNAME")
    


    if not sender or not os.getenv("SMTP_USERNAME") or not os.getenv("SMTP_PASSWORD"):
        raise RuntimeError("SMTP credentials are not configured")
    
    html_body = _render_template("password_changed_email.html")
    text_body = "Hi there\n\nYou have successfully changed your password."
    msg = _build_message("Password Changed Successfully", sender, to_email, text_body, html_body)

    _send_message(msg, sender, to_email)
