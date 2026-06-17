import schedule
import time
from datetime import datetime
from fb_connect import db
from twilio.rest import Client
from dotenv import load_dotenv
import os
import urllib.parse

# Load .env
load_dotenv()

# Twilio env variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP")
TWILIO_SMS = os.getenv("TWILIO_SMS")
TWILIO_CALL = os.getenv("TWILIO_CALL")
USER_PHONE = os.getenv("USER_PHONE")

# Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH)


def send_whatsapp(title, description):
    message = f"🔔 Reminder:\n{title}\n\n{description}"
    client.messages.create(
        from_=TWILIO_WHATSAPP,
        to=f"whatsapp:{USER_PHONE}",
        body=message
    )
    print("WhatsApp sent")


def send_sms(title, description):
    message = f"Reminder:\n{title}\n{description}"
    client.messages.create(
        from_=TWILIO_SMS,
        to=USER_PHONE,
        body=message
    )
    print("SMS sent")


def send_call(title, description):
    # URL Encode for safety
    title_enc = urllib.parse.quote(title)
    desc_enc = urllib.parse.quote(description)

    call_url = f"http://127.0.0.1:5000/call_voice?title={title_enc}&description={desc_enc}"

    client.calls.create(
        url=call_url,
        to=USER_PHONE,
        from_=TWILIO_CALL
    )
    print("Call initiated with voice message")
    import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(title, description):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ID
    msg["To"] = USER_EMAIL
    msg["Subject"] = f"Reminder: {title}"

    body = f"""
🔔 Reminder

Title: {title}
Description: {description}
    """

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ID, EMAIL_PASS)
        server.send_message(msg)

    print("✅ Email sent")



def check_reminders():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    reminders = db.collection("reminders") \
        .where("status", "==", "pending") \
        .stream()

    for reminder in reminders:
        data = reminder.to_dict()
        reminder_time = f"{data['date']} {data['time']}"

        if reminder_time == now:
            print(f"Reminder Triggered: {data['title']}")

            # Mark reminder as sent in Firebase
            db.collection("reminders").document(reminder.id).update({
                "status": "sent",
                "sent_at": datetime.now().isoformat()
            })

            # Send notifications
            if data["delivery"] == "WhatsApp":
                send_whatsapp(data["title"], data["description"])

            elif data["delivery"] == "SMS":
                send_sms(data["title"], data["description"])

            elif data["delivery"] == "Call":
                send_call(data["title"], data["description"])

            elif data["delivery"] == "Email":
                send_email(data["title"], data["description"])


            else:
                print("Unknown delivery method")


# Scheduler runs every minute
schedule.every(1).minutes.do(check_reminders)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)
