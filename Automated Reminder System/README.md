# 📧 Automatic Email Reminder App

A multi-channel reminder system that notifies users via **Email, SMS, and Call**, so important tasks, deadlines, and meetings are never missed.

Built with **Python Flask** and **PostgreSQL**, the app lets users register, log in, and schedule reminders that are automatically triggered at the right time through their preferred notification channel.

---

## ✨ Features

- 🔐 **User Authentication** — Secure register/login powered by Firebase Authentication
- ☁️ **Cloud Database** — Reminder data stored and synced via Firebase (Firestore / Realtime Database)
- 📝 **Custom Reminders** — Set title, message, date, time, email, and phone number
- 📡 **Multi-Channel Notifications** — Choose Email, SMS, Call, or All
- ⏰ **Automated Scheduling** — Powered by APScheduler for accurate, hands-free triggering
- 📬 **Email Alerts** — Sent via the SendGrid API
- 📱 **SMS & Call Alerts** — Sent via the Twilio API
- ☁️ **Cloud Deployable** — Ready for free hosting on Render or Railway
- 📱 **Responsive UI** — Built with Bootstrap / Tailwind CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend Framework | Flask |
| Authentication | Firebase Authentication |
| Database | Firebase (Firestore / Realtime Database) |
| Scheduler | APScheduler |
| Email Service | SendGrid API |
| SMS / Call Service | Twilio API |
| Frontend | HTML, CSS, Bootstrap / Tailwind CSS |
| Deployment | Render / Railway |

---

## 🧩 How It Works

1. A user registers and logs in via **Firebase Authentication**.
2. They create a reminder with a title, message, date, time, and contact details — stored in **Firebase** (Firestore / Realtime Database).
3. They select a notification mode — **Email**, **SMS**, **Call**, or **All**.
4. **APScheduler** continuously monitors Firebase for upcoming reminders in the background.
5. When the scheduled time arrives, the system automatically sends the reminder through the selected channel(s):
   - **Email** → SendGrid API
   - **SMS / Call** → Twilio API

---

## 📸 Screenshots

> _Add input and output screenshots here_

| Input Screen | Output Screen |
|---|---|
| ![Input Screen](#) | ![Output Screen](#) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A Firebase project (with Authentication and Firestore/Realtime Database enabled)
- SendGrid API key
- Twilio API key (Account SID, Auth Token, phone number)

### Installation

```bash
# Clone the repository
git clone https://github.com/tanmay1113/automatic-email-reminder-app.git
cd automatic-email-reminder-app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Firebase Setup

1. Create a project in the [Firebase Console](https://console.firebase.google.com/).
2. Enable **Authentication** (Email/Password, or your preferred sign-in method).
3. Enable **Firestore** or **Realtime Database** for storing reminders.
4. Generate a **service account key** (Project Settings → Service Accounts → Generate new private key) and save it as `firebase-credentials.json` in the project root (keep this file out of version control).
5. Copy your Firebase **web app config** for use in the frontend if needed (API key, project ID, etc.).

### Configuration

Create a `.env` file in the project root and add your credentials:

```env
FIREBASE_CREDENTIALS=firebase-credentials.json
FIREBASE_PROJECT_ID=your_firebase_project_id
SENDGRID_API_KEY=your_sendgrid_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
SECRET_KEY=your_flask_secret_key
```

### Run the App

```bash
flask run
```

The app will be available at `http://127.0.0.1:5000`.

---

## 🌱 Future Scope

- 📲 WhatsApp reminders via the official WhatsApp Cloud API
- 🔁 Recurring reminders (daily, weekly, monthly)
- 📅 Google Calendar integration for automatic event sync
- 📱 Mobile app version for Android and iOS
- 🗣️ Voice assistant integration (Google Assistant, Alexa)
- 🤖 AI-based scheduling that predicts reminder times from user patterns
- 🔑 OAuth login using Google or Microsoft accounts
- 🔒 End-to-end encryption for sensitive user data

---

## ⚠️ Limitations

- Requires a stable internet connection for Firebase and API-based notifications
- Free tiers of Firebase, SendGrid, and Twilio have daily usage limits
- The web app must stay active for scheduled reminders to trigger
- No offline storage or notifications if the backend server is down
- Scalability to enterprise-level usage may require further optimization
- User data security depends on Firebase security rules and configuration

---

## 📚 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [APScheduler Documentation](https://apscheduler.readthedocs.io/)
- [SendGrid API](https://docs.sendgrid.com/)
- [Twilio API](https://www.twilio.com/docs)
- [Bootstrap Framework](https://getbootstrap.com/)
- [Python Official Documentation](https://docs.python.org/3/)

---

## 👥 Authors

- **Tanmay Bhole**
- **Vedant Warade**

S.Y.B.Sc. (Information Technology), Semester III — Mini Project (IT231FP)
Savitribai Phule Pune University, 2025–26

---
