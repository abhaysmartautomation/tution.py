import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY SETTINGS ---
INSTITUTE_NAME = "🌟 *PRINCE ACADEMY* 🌟"
CONTACT_NO = "+91 98765-43210"
TIMING = "🕘 08:00 AM - 🕗 08:00 PM"
UPI_ID = "princeacademy@upi" # Aapki UPI ID
PAYMENT_NAME = "Prince Academy"

# --- 🖼️ IMAGE GENERATOR ---
def get_image_link(text):
    clean_text = text.replace(" ", "+")
    return f"https://placehold.co/600x800/png?text={clean_text}&font=roboto"

@app.route('/')
def home():
    return "🦁 Prince Academy Bot is Online & Debugged!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    # User message clean up
    msg = request.args.get('msg', '').lower().strip()
    
    # 1️⃣ START / MENU
    if msg in ['hi', 'hello', 'hey', 'start', 'menu', 'namaste']:
        return (f"{INSTITUTE_NAME}\n\n"
                "Hello! Main *Prince Academy* ka smart assistant hoon. 🤖\n"
                "Aapko kaise sahayata chahiye?\n\n"
                "📚 *CLASSES INFO (6-12)*\n"
                "👉 Type karein: *6, 7, 8, 9, 10, 11 ya 12*\n\n"
                "💳 *PAYMENT & FEES*\n"
                "👉 Type karein: *Payment*\n\n"
                "❓ *QUERY & ADMISSION*\n"
                "👉 Type karein: *Query*")

    # 2️⃣ PAYMENT & FEES SYSTEM 💳
    if 'payment' in msg or 'fees' in msg or 'pay' in msg:
        return (f"💳 *PAYMENT INFORMATION*\n"
                f"---------------------------\n"
                f"Aap apni fees niche diye gaye options se jama kar sakte hain:\n\n"
                f"🆔 *UPI ID:* `{UPI_ID}`\n"
                f"👤 *Name:* {PAYMENT_NAME}\n\n"
                f"💰 *GPay/PhonePe:* {CONTACT_NO}\n"
                f"⚠️ *Note:* Payment ke baad screenshot isi number par bhej dein.\n\n"
                f"🔗 *Payment QR:* {get_image_link('SCAN+TO+PAY+FEES')}")

    # 3️⃣ QUERY & ADMISSION HELP 📞
    if 'query' in msg or 'admission' in msg or 'help' in msg:
        return (f"📞 *HELP DESK & ADMISSION*\n"
                f"---------------------------\n"
                f"📍 *Location:* Prince Classes, Main Road.\n"
                f"⏰ *Timing:* {TIMING}\n"
                f"📱 *Call:* {CONTACT_NO}\n\n"
                f"📑 *Online Admission Form:* \n"
                f"https://forms.gle/DemoAdmissionForm\n\n"
                f"Main menu ke liye *Hi* likhein.")

    # 4️⃣ CLASS SELECTION LOGIC
    classes = ['6', '7', '8', '9', '10', '11', '12']
    
    # Check for direct class number (e.g., "10")
    if msg in classes:
        return (f"📂 *CLASS {msg} MENU*\n"
                f"---------------------------\n"
                f"Kya dekhna chahte hain? Type karein:\n\n"
                f"📝 *Exam {msg}* (Exam Info)\n"
                f"📅 *Schedule {msg}* (Routine)\n"
                f"🕒 *Time {msg}* (Time Table)")

    # 5️⃣ DETAILED CLASS INFO (e.g., "Time 10")
    detected_class = None
    for c in classes:
        if c in msg:
            detected_class = c
            break
            
    if detected_class:
        if 'exam' in msg:
            return f"📝 *Class {detected_class} Exam Plan:*\nDownload: {get_image_link(f'Class+{detected_class}+Exam+Plan')}"
        elif 'schedule' in msg:
            return f"📅 *Class {detected_class} Regular Schedule:*\nDownload: {get_image_link(f'Class+{detected_class}+Schedule')}"
        elif 'time' in msg:
            return f"🕒 *Class {detected_class} Time Table:*\nDownload: {get_image_link(f'Class+{detected_class}+Time+Table')}"

    # 6️⃣ SMART FALLBACK (Unknown Message)
    return ("⚠️ *Maaf karein!* Mujhse galti ho gayi.\n\n"
            "Kripya sahi word likhein ya niche options dekhein:\n"
            "✅ *Hi* - Main Menu\n"
            "✅ *10* - Class 10 Info\n"
            "✅ *Payment* - Fees details")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
