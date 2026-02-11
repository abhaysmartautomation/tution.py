import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY CONFIGURATION ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"
UPI_ID = "prince@upi" # Apni UPI ID badal dein
PHONE = "+91 98765-43210" # Apna Number badal dein
FORM = "https://forms.gle/XYZ123DemoForm"

def get_img(txt):
    return f"https://placehold.co/600x800/png?text={txt.replace(' ', '+')}&font=roboto"

@app.route('/')
def home():
    return "Bot is Online & Robust!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    msg = request.args.get('msg', '').lower().strip()
    
    # 🛑 Filter for system errors
    if not msg or "{not_text}" in msg or "[not_text]" in msg:
        return ""

    # 1️⃣ START / MENU / HI
    greetings = ['hi', 'hello', 'hey', 'start', 'menu', 'namaste', 'hlw']
    if any(word == msg for word in greetings):
        return (f"{NAME}\n{LINE}\n"
                "Aapko kis class ki jankari chahiye?\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Fees, Admission, Timing)\n\n"
                "👉 *Sirf number likh kar bhejein*")

    # 2️⃣ SMART QUERY SECTION (Admission, Payment, Fees)
    help_words = ['query', 'help', 'admission', 'payment', 'fees', 'timing', 'pay', 'address']
    if any(word in msg for word in help_words):
        # Specific sub-replies for Payment/Admission
        if 'pay' in msg or 'fees' in msg:
            return (f"💳 *FEES & PAYMENT*\n{LINE}\n"
                    f"🆔 *UPI ID:* `{UPI_ID}`\n"
                    f"💰 *GPay/PhonePe:* {PHONE}\n"
                    "⚠️ *Note:* Payment ke baad screenshot isi number par bhej dein.")
        
        if 'admission' in msg:
            return (f"📝 *NEW ADMISSION*\n{LINE}\n"
                    f"🔗 *Form Link:* {FORM}\n"
                    "Kripya form bharein, hum aapse sampark karenge.")

        return (f"❓ *HELP DESK*\n{LINE}\n"
                f"⏰ *Timing:* 8 AM to 8 PM\n"
                f"📍 *Address:* City Center, Main Road.\n"
                f"📞 *Contact:* {PHONE}\n\n"
                "Menu ke liye *Hi* likhein.")

    # 3️⃣ SMART CLASS DETECTION (6-12)
    classes = ['6', '7', '8', '9', '10', '11', '12']
    detected = next((c for c in classes if c in msg), None)

    if detected:
        # Check for specific topics
        if 'time' in msg or 'table' in msg:
            return f"🕒 *CLASS {detected} TIME TABLE*\n{LINE}\n📥 {get_img(f'Class {detected} Time Table')}"
        
        elif 'exam' in msg or 'date' in msg or 'test' in msg:
            return f"📝 *CLASS {detected} EXAM PLAN*\n{LINE}\n📥 {get_img(f'Class {detected} Exam Schedule')}"
        
        else:
            # Show sub-menu for the specific class
            return (f"📂 *CLASS {detected} MENU*\n{LINE}\n"
                    "Aapko kya chahiye? Type karein:\n\n"
                    f"👉 *Time {detected}*\n"
                    f"👉 *Exam {detected}*\n"
                    f"👉 *Fees {detected}*")

    # 4️⃣ FALLBACK (If nothing matches)
    return ("⚠️ *Samajh nahi aaya!*\n\n"
            "Kripya sahi number (6-12) likhein ya *Hi* bhej kar menu dekhein.")

if __name__ == '__main__':
    # Fixed Port Binding for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
