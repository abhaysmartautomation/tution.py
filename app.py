import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY DETAILS ---
INSTITUTE_NAME = "🌟 *PRINCE ACADEMY* 🌟"
CONTACT = "+91 98765-43210"
TIMING = "🕘 8 AM - 🕗 8 PM"
UPI = "prince@upi"
FORM = "https://forms.gle/DemoForm"

def get_img(text):
    return f"https://placehold.co/600x800/png?text={text.replace(' ', '+')}&font=roboto"

@app.route('/')
def home(): return "Prince Academy Bot is Active!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    msg = request.args.get('msg', '').lower().strip()
    
    # 1. Welcome Menu (Line by Line)
    if msg in ['hi', 'hello', 'hey', 'start', 'menu']:
        return (f"{INSTITUTE_NAME}\n"
                "---------------------------\n"
                "Kripya niche se chunein:\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n"
                "❓ - Query (Fees, Admission, Timing)\n\n"
                "👉 *Sirf number bhejye (Ex: 10)*")

    # 2. Query Section (Admission + Payment + Timing)
    if 'query' in msg or 'help' in msg or '?' in msg:
        return (f"❓ *HELP & ADMISSION*\n"
                f"---------------------------\n"
                f"⏰ *Timing:* {TIMING}\n"
                f"📝 *Admission Form:* {FORM}\n"
                f"💳 *Fees Payment:* `{UPI}`\n"
                f"📞 *Call:* {CONTACT}\n\n"
                f"Main menu ke liye *Hi* likhein.")

    # 3. Handle Class Number (6, 7, 8...)
    classes = ['6', '7', '8', '9', '10', '11', '12']
    if msg in classes:
        return (f"📂 *CLASS {msg} MENU*\n"
                "---------------------------\n"
                f"Kya dekhna hai? Type karein:\n\n"
                f"👉 *Time {msg}* (Time Table)\n"
                f"👉 *Exam {msg}* (Exam Date)\n"
                f"👉 *Fees {msg}* (Fees Detail)")

    # 4. Handle Specific Topics (Time 10, Exam 10, Fees 10)
    detected_class = None
    for c in classes:
        if c in msg:
            detected_class = c
            break
            
    if detected_class:
        if 'time' in msg:
            return f"🕒 *Class {detected_class} Time Table:*\nDownload: {get_img(f'Class {detected_class} Time Table')}"
        elif 'exam' in msg:
            return f"📝 *Class {detected_class} Exam Plan:*\nDownload: {get_img(f'Class {detected_class} Exam Plan')}"
        elif 'fees' in msg or 'payment' in msg:
            return f"💳 *Class {detected_class} Fees:* ₹2000/month\nPay to: {UPI}"

    # 5. Simple Fallback
    return "⚠️ *Samajh nahi aaya.*\n\nMain menu ke liye *Hi* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
