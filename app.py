import os
from flask import Flask, request

app = Flask(__name__)

# --- CONFIGURATION ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"

@app.route('/')
def home(): return "Prince Academy Bot is Live!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    # Message clean up
    msg = request.args.get('msg', '').lower().strip()
    
    # 1. Main Menu (Simple List)
    if msg in ['hi', 'hello', 'start', 'namaste', 'hlw']:
        return (f"{NAME}\n{LINE}\n"
                "Namaste! Niche se option chunein:\n\n"
                "6️⃣ - Class 6 info\n7️⃣ - Class 7 info\n8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n🔟 - Class 10 info\n1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Admission/Payment/Timing)\n\n"
                "👉 *Sirf number likh kar bhejein*")

    # 2. Query/Admission/Payment (All in one)
    if 'query' in msg or 'admission' in msg or 'payment' in msg:
        return (f"❓ *HELP & ADMISSION*\n{LINE}\n"
                f"⏰ *Timing:* 8 AM - 8 PM\n"
                f"📝 *Admission Form:* bit.ly/DemoForm\n"
                f"💳 *UPI ID:* `prince@upi`\n"
                f"📞 *Contact:* 9876543210\n\n"
                "Main menu ke liye *Hi* likhein.")

    # 3. Class Logic (Simple)
    classes = ['6', '7', '8', '9', '10', '11', '12']
    if msg in classes:
        return (f"📂 *CLASS {msg} INFO*\n{LINE}\n"
                "Type karein:\n"
                f"👉 *Time {msg}*\n"
                f"👉 *Exam {msg}*")

    # 4. Detailed Data
    detected = next((c for c in classes if c in msg), None)
    if detected:
        if 'time' in msg:
            return f"🕒 *CLASS {detected} TIME TABLE*\n{LINE}\nCheck here: https://placehold.co/600x800/png?text=Class+{detected}+Time+Table"
        elif 'exam' in msg:
            return f"📝 *CLASS {detected} EXAM PLAN*\n{LINE}\nCheck here: https://placehold.co/600x800/png?text=Class+{detected}+Exam"

    # Fallback
    return "⚠️ *Maaf karein, samajh nahi aaya.*\n\nMain menu ke liye *Hi* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
