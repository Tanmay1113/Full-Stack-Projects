from flask import Flask, request, jsonify, render_template, Response
from fb_connect import db
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Twilio settings
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP")
USER_PHONE = os.getenv("USER_PHONE")

# Create Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH)

app = Flask(__name__, template_folder="templates", static_folder="static")


# Homepage route
@app.route("/")
def home():
    return render_template("dashboard.html")


# WhatsApp Message Sender
def send_whatsapp(message):
    client.messages.create(
        from_=TWILIO_WHATSAPP,
        to=f"whatsapp:{USER_PHONE}",
        body=message
    )


@app.route("/add_reminder", methods=["POST"])
def add_reminder():
    data = request.json

    # Field validation
    required = ["title", "date", "time", "delivery"]
    for field in required:
        if field not in data or not data[field]:
            return jsonify({"message": f"ERROR: Missing field: {field}"}), 400

    # Create new document with auto-generated ID
    ref = db.collection("reminders").document()
    ref.set({
        "title": data["title"],
        "description": data.get("description", ""),
        "date": data["date"],
        "time": data["time"],
        "delivery": data["delivery"],
        "status": "pending"
    })

    return jsonify({
        "message": "Reminder stored in Firebase!",
        "id": ref.id
    })


@app.route("/call_voice")
def call_voice():
    title = request.args.get("title", "No title provided")
    description = request.args.get("description", "No description provided")

    twiml = f"""
    <Response>
        <Say voice="alice">
            Reminder Alert. {title}. {description}.
        </Say>
    </Response>
    """

    return Response(twiml, mimetype="text/xml")


if __name__ == "__main__":
    app.run(debug=True)
