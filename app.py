import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY CONFIGURATION ---
INSTITUTE_NAME = "🌟 *PRINCE ACADEMY* 🌟"
ADDRESS = "📍 Address: City Center, Main Road, Surat."
CONTACT_NO = "+91 98765-43210"
TIMING = "🕘 8:00 AM to 🕗 8:00 PM"
FORM_LINK = "https://forms.gle/XYZ123DemoForm" 
UPI_ID = "princeacademy@upi"

def get_image_link(text):
    clean_text = text.replace(" ", "+")
    return f"https://placehold.co/600x800/png?text={clean_text}&font=roboto"

@app.route('/')
def home():
    return "🦁 Prince Academy Bot is Online & Simple!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    msg = request.args.get('msg', '').lower().strip()
    
    # 1️⃣ MAIN MENU (Line-by-line with 'info' text)
    greetings = ['hi', 'hello', 'hey', 'start', 'namaste', 'hlw']
    if any(word == msg for word in greetings):
        return (f"{INSTITUTE_NAME}\n"
                f"---------------------------\n"
                "Hello! Main *Prince Academy Bot* hoon. 🤖\n"
                "Aapko kis class ki jankari chahiye?\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Admission, Payment, Timing)\n\n"
                "👉 *Sirf number ya 'Query' likh kar bhejye*")

    # 2️⃣ QUERY SECTION (Includes Admission & Payment)
    if 'query' in msg or 'help' in msg:
        return (f"❓ *PRINCE ACADEMY - HELP DESK*\n"
                f"---------------------------\n"
                f"Aapki help ke liye niche options hain:\n\n"
                f"📝 *Admission:* Type karein 'Admission'\n"
                f"💳 *Payment:* Type karein 'Payment'\n"
                f"⏰ *Timing:* {TIMING}\n"
                f"📱 *Contact:* {CONTACT_NO}\n"
                f"{ADDRESS}\n\n"
                f"Main menu ke liye *Hi* likhein.")

    # 3️⃣ ADMISSION OPTION
    if 'admission' in msg:
        return (f"📝 *NEW ADMISSION FORM*\n"
                f"---------------------------\n"
                f"Naye batches shuru ho gaye hain!\n\n"
                f"🔗 *Form Link:* {FORM_LINK}\n"
                f"Kripya ise bharein, hum sampark karenge.")

    # 4️⃣ PAYMENT OPTION
    if 'payment' in msg or 'fees' in msg:
        return (f"💳 *FEES PAYMENT DETAILS*\n"
                f"---------------------------\n"
                f"🆔 *UPI ID:* `{UPI_ID}`\n"
                f"💰 *GPay/PhonePe:* {CONTACT_NO}\n\n"
                f"⚠️ *Note:* Payment ke baad screenshot bhejna na bhoolein.")

    # 5️⃣ CLASS SELECTION HANDLING (Handles '6' or 'class 6')
    classes = ['6', '7', '8', '9', '10', '11', '12']
    detected_num = None
    for c in classes:
        if c == msg or f"class {c}" in msg:
            detected_num = c
            break
            
    if detected_num:
        return (f"📂 *CLASS {detected_num} - MENU*\n"
                f"---------------------------\n"
                f"Kya dekhna chahte hain? Type karein:\n\n"
                f"📝 *Exam {detected_num}*\n"
                f"📅 *Schedule {detected_num}*\n"
                f"🕒 *Time {detected_num}*")

    # 6️⃣ TOPIC HANDLING (Time 10, Exam 10 etc.)
    detected_class = None
    for c in classes:
        if c in msg:
            detected_class = c
            break
            
    if detected_class:
        if 'exam' in msg:
            return f"📝 *Class {detected_class} Exam Plan:*\nCheck here: {get_image_link(f'Class+{detected_class}+Exam+Schedule')}"
        elif 'schedule' in msg:
            return f"📅 *Class {detected_class} Regular Schedule:*\nCheck here: {get_image_link(f'Class+{detected_class}+Schedule')}"
        elif 'time' in msg:
            return f"🕒 *Class {detected_class} Time Table:*\nCheck here: {get_image_link(f'Class+{detected_class}+Time+Table')}"

    # 7️⃣ FALLBACK
    return ("⚠️ *Maaf karein, samajh nahi aaya!*\n\n"
            "Sahi command likhein ya *Hi* bhej kar menu dekhein.")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
