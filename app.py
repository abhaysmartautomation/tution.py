import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 ACADEMY INFO ---
NAME = "🌟 *PRINCE ACADEMY* 🌟"
LINE = "---------------------------"
UPI = "prince@upi"
CONTACT = "9876543210"

def get_img(topic):
    # Attractive placeholder image logic
    return f"https://placehold.co/600x800/png?text={topic.replace(' ', '+')}&font=roboto"

@app.route('/')
def home(): return "Bot is Active!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    msg = request.args.get('msg', '').lower().strip()
    
    # 1️⃣ MAIN MENU (Simple & Line-by-line)
    if msg in ['hi','hii', 'hello', 'hey', 'start', 'menu']:
        return (f"{NAME}\n{LINE}\n"
                "Aapko kis class ki info chahiye?\n\n"
                "6️⃣ - Class 6 info\n"
                "7️⃣ - Class 7 info\n"
                "8️⃣ - Class 8 info\n"
                "9️⃣ - Class 9 info\n"
                "🔟 - Class 10 info\n"
                "1️⃣1️⃣ - Class 11 info\n"
                "1️⃣2️⃣ - Class 12 info\n\n"
                "❓ - *Query* (Fees/Admission)\n\n"
                "👉 *jankari ke liye Sirf Number bhejein (Ex: 10,11,12...)*")

    # 2️⃣ QUERY SECTION (All in one place)
    if msg == 'query','quary','jankari','info'' or msg == 'help':
        return (f"❓ *HELP & ADMISSION*\n{LINE}\n"
                f"⏰ *Timing:* 8 AM - 8 PM\n"
                f"📝 *Admission:* Link niche hai\n"
                f"💳 *Payment UPI:* `{UPI}`\n"
                f"📞 *Call:* {CONTACT}\n\n"
                "Main menu ke liye *Hi,hello,start,menu* likhein.")

    # 3️⃣ CLASS SUB-MENU (Direct & Same Format)
    classes = ['6', '7', '8', '9', '10', '11', '12']
    if msg in classes:
        return (f"📂 *CLASS {msg} MENU*\n{LINE}\n"
                "Kya dekhna chahte hain? Type karein:\n\n"
                f"👉 *Time {msg}* (Time Table)\n"
                f"👉 *Exam {msg}* (Exam Date)\n"
                f"👉 *Fees {msg}* (Fees Detail)")

    # 4️⃣ FINAL DATA (Time, Exam, Fees)
    # Check if message contains both class and topic
    found_class = next((c for c in classes if c in msg), None)
    
    if found_class:
        if 'time' in msg:
            return (f"🕒 *CLASS {found_class} TIME TABLE*\n{LINE}\n"
                    "Ye raha aapka schedule:\n"
                    f"📥 {get_img(f'Class {found_class} Time Table')}")
        
        elif 'exam' in msg:
            return (f"📝 *CLASS {found_class} EXAM PLAN*\n{LINE}\n"
                    "Exam ki taiyari shuru karein:\n"
                    f"📥 {get_img(f'Class {found_class} Exam Plan')}")
            
        elif 'fees' in msg or 'payment' in msg:
            return (f"💳 *CLASS {found_class} FEES*\n{LINE}\n"
                    "Fees: ₹2000/Month\n"
                    f"Pay to UPI: `{UPI}`\n"
                    "Screenshot isi number par bhejein.")

    # 5️⃣ FALLBACK (Simple Error)
    return "⚠️ *Samajh nahi aaya.*\n\nMain menu ke liye *Hi,helo,menu,start* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
