import os
from flask import Flask, request

app = Flask(__name__)

# --- CONFIG ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"
UPI = "prince@upi"

def get_img(txt):
    return f"https://placehold.co/600x800/png?text={txt.replace(' ', '+')}&font=roboto"

@app.route('/')
def home(): 
    return "Prince Academy Bot is Live!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    msg = request.args.get('msg', '').lower().strip()
    
    # Simple Logic
    if msg in ['hi', 'hello', 'start', 'menu', 'namaste']:
        return (f"{NAME}\n{LINE}\n"
                "Aapko kis class ki info chahiye?\n\n"
                "6️⃣ - Class 6 info\n7️⃣ - Class 7 info\n8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n🔟 - Class 10 info\n1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Admission/Fees)\n\n"
                "👉 *Sirf number likh kar bhejye*")

    # Handle Class
    classes = ['6', '7', '8', '9', '10', '11', '12']
    detected = next((c for c in classes if c in msg), None)
    
    if detected:
        if 'time' in msg:
            return f"🕒 *CLASS {detected} TIME TABLE*\n{LINE}\n📥 {get_img(f'Class {detected} Time Table')}"
        elif 'exam' in msg:
            return f"📝 *CLASS {detected} EXAM PLAN*\n{LINE}\n📥 {get_img(f'Class {detected} Exam')}"
        elif 'fees' in msg or 'payment' in msg:
            return f"💳 *CLASS {detected} FEES*\n{LINE}\nFees: ₹2000\nUPI: `{UPI}`"
        else:
            return (f"📂 *CLASS {detected} MENU*\n{LINE}\n"
                    f"👉 *Time {detected}*\n👉 *Exam {detected}*\n👉 *Fees {detected}*")

    return "⚠️ *Maaf karein, samajh nahi aaya.*\nMain menu ke liye *Hi* likhein."

if __name__ == '__main__':
    # Render ke liye ye settings zaroori hain
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
