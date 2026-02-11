import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY CONFIG ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"
UPI = "prince@upi"
CONTACT = "9876543210"

def get_img(txt):
    return f"https://placehold.co/600x800/png?text={txt.replace(' ', '+')}&font=roboto"

@app.route('/')
def home(): return "Bot is Online!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    # User message cleanup
    msg = request.args.get('msg', '').lower().strip()
    
    # 1️⃣ MAIN MENU (Simple Line-by-Line)
    greetings = ['hi','hii', 'hello', 'hey', 'start', 'menu', 'namaste']
    if any(word == msg for word in greetings):
        return (f"{NAME}\n{LINE}\n"
                "Aapko kis class ki info chahiye?\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Admission/Fees)\n\n"
                "👉 *Sirf number likh kar bhejein*")

    # 2️⃣ QUERY SECTION (Simplified All-in-one)
    if 'query' in msg or 'help' in msg:
        return (f"❓ *HELP & ADMISSION*\n{LINE}\n"
                f"⏰ *Timing:* 8 AM - 8 PM\n"
                f"💳 *Fees Payment:* `{UPI}`\n"
                f"📝 *Admission Form:* bit.ly/DemoForm\n"
                f"📞 *Call:* {CONTACT}\n\n"
                "Main menu ke liye *Hi* likhein.")

    # 3️⃣ CLASS & TOPIC LOGIC (Smart Detection)
    classes = ['6', '7', '8', '9', '10', '11', '12','class 6', 'class 7', 'class 8', 'class 9', 'class 10', 'class 11', 'class 12']
    
    # Check if user only sent a class number (e.g., "10" or "10 info")
    for c in classes:
        if msg == c or msg == f"{c} info" or msg == f"class {c} info":
            return (f"📂 *CLASS {c} MENU*\n{LINE}\n"
                    "Kya jankari chahiye? Type karein:\n\n"
                    f"👉 *Time {c}* (Time Table)\n"
                    f"👉 *Exam {c}* (Exam Date)\n"
                    f"👉 *Fees {c}* (Fees Detail)")

    # 4️⃣ RELATIVE SEARCH (e.g., "Time 10")
    detected_class = next((c for c in classes if c in msg), None)
    if detected_class:
        if 'time' in msg:
            return f"🕒 *CLASS {detected_class} TIME TABLE*\n{LINE}\n📥 {get_img(f'Class {detected_class} Time Table')}"
        elif 'exam' in msg:
            return f"📝 *CLASS {detected_class} EXAM PLAN*\n{LINE}\n📥 {get_img(f'Class {detected_class} Exam Plan')}"
        elif 'fees' in msg or 'payment' in msg:
            return f"💳 *CLASS {detected_class} FEES*\n{LINE}\nMonthly Fees: ₹7000\nPay to UPI: `{UPI}`"

    # 5️⃣ FALLBACK
    return "⚠️ *Maaf karein, samajh nahi aaya.*\n\nMain menu ke liye *Hi,hello,menu* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
