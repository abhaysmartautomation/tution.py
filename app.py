import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 SETTINGS ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"
CONTACT = "9876543210"
UPI = "prince@upi"

def get_img(text):
    return f"https://placehold.co/600x800/png?text={text.replace(' ', '+')}&font=roboto"

@app.route('/')
def home(): return "Prince Academy Bot is Live!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    # Message ko clean karna (Spaces hatana)
    msg = request.args.get('msg', '').lower().strip()
    
    # 1️⃣ MAIN MENU (Simple line by line)
    if msg in ['hi', 'hii','hello', 'hey', 'start', 'menu']:
        return (f"{NAME}\n{LINE}\n"
                "Aapko kis class ki info chahiye?\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Admission/Payment)\n\n"
                "👉 *Sirf number likh kar bhejein(eg 6,7,8,9,10)*")

    # 2️⃣ QUERY SECTION (Simple & All-in-one)
    if msg == 'query' or msg == 'help':
        return (f"❓ *HELP & ADMISSION*\n{LINE}\n"
                f"⏰ *Timing:* 8 AM - 8 PM\n"
                f"📝 *Admission:* Link niche hai\n"
                f"💳 *Fees Payment:* `{UPI}`\n"
                f"📞 *Call:* {CONTACT}\n\n"
                "Main menu ke liye *Hi* likhein.")

    # 3️⃣ CLASS SUB-MENU (Direct)
    classes = ['class 6', 'class 7', 'class 8', 'class 9', 'class 10', 'class 11', 'class 12','6', '7', '8', '9', '10', '11', '12']
    if msg in classes:
        return (f"📂 *CLASS {msg} MENU*\n{LINE}\n"
                "Kya dekhna chahte hain? Type karein:\n\n"
                f"👉 *Time {msg}*\n"
                f"👉 *Exam {msg}*\n"
                f"👉 *Fees {msg}*")

    # 4️⃣ FINAL DATA HANDLING (Related & Clear)
    found_class = next((c for c in classes if c in msg), None)
    
    if found_class:
        if 'time' in msg:
            return f"🕒 *CLASS {found_class} TIME TABLE*\n{LINE}\n📥 {get_img(f'Class {found_class} Time Table')}"
        elif 'exam' in msg:
            return f"📝 *CLASS {found_class} EXAM PLAN*\n{LINE}\n📥 {get_img(f'Class {found_class} Exam Plan')}"
        elif 'fees' in msg or 'payment' in msg:
            return f"💳 *CLASS {found_class} FEES*\n{LINE}\nFees: ₹2000/Month\nPay: `{UPI}`"

    # 5️⃣ SMART FALLBACK (Agar kuch na mile)
    return "⚠️ *Maaf karein, samajh nahi aaya.*\n\nMain menu ke liye *Hi,hello ,menu * likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
