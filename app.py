from flask import Flask, request
import re

app = Flask(__name__)

# ---------------------------------------------------------
# 👇 ADMIN SETTINGS
# ---------------------------------------------------------

PHONE_NO = "9898308806"

# 1. TIME TABLE LINKS
TIMETABLE_LINKS = {
    '6': "https://bit.ly/Prince-Class6", '7': "https://bit.ly/Prince-Class7",
    '8': "https://bit.ly/Prince-Class8", '9': "https://bit.ly/Prince-Class9",
    '10': "https://bit.ly/Prince-Class10", '11': "https://bit.ly/Prince-Class11",
    '12': "https://bit.ly/Prince-Class12"
}

# 2. EXAM SCHEDULE LINKS
EXAM_LINKS = {
    '6': "https://bit.ly/Exam-Class6", '7': "https://bit.ly/Exam-Class7",
    '8': "https://bit.ly/Exam-Class8", '9': "https://bit.ly/Exam-Class9",
    '10': "https://bit.ly/Exam-Class10", '11': "https://bit.ly/Exam-Class11",
    '12': "https://bit.ly/Exam-Class12"
}

# 3. GLOBAL & CLASS NOTICES
current_notices = {
    'all': "Sab normal", 
    '6': "Sab normal", '7': "Sab normal", '8': "Sab normal",
    '9': "Sab normal", '10': "Sab normal", '11': "Sab normal", '12': "Sab normal"
}

# ---------------------------------------------------------

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    msg = request.args.get('msg', '').strip()
    msg_lower = msg.lower()

    # --- 👑 ADMIN COMMAND ---
    if msg_lower.startswith("set notice"):
        try:
            parts = msg.split(" ", 3)
            target = parts[2].lower()
            new_notice = parts[3]
            if target in current_notices:
                current_notices[target] = new_notice
                return f"✅ *Success!* Notice updated for {target.upper()}"
        except:
            return "❌ Error! Format: *set notice 10 My Message*"

    # --- 🤖 SMART KEYWORDS ---
    greet_words = ['hi', 'hello', 'hey', 'namaste', 'menu', 'start', 'hii', 'helo', 'hy', 'shuru']
    pay_words   = ['payment', 'pay', 'fee', 'fees', 'fess', 'paisa', 'money', 'qr', 'upi', 'bank']
    info_words  = ['timetable', 'time table', 'schedule', 'routine', 'exam', 'test', 'paper', 'datesheet', 'timing']

    # Smart Class Number Finder
    numbers_found = re.findall(r'\d+', msg_lower)
    valid_class = None
    if numbers_found:
        for num in numbers_found:
            if num in TIMETABLE_LINKS:
                valid_class = num
                break

    # 🟢 1. CLASS DASHBOARD
    if valid_class:
        class_num = valid_class
        t_link = TIMETABLE_LINKS.get(class_num)
        e_link = EXAM_LINKS.get(class_num)
        active_notice = current_notices.get(class_num, "Sab normal")
        
        notice_box = ""
        if "Sab normal" not in active_notice:
            notice_box = f"╔══════════════════╗\n📢  *CLASS {class_num} NOTICE*\n\n  {active_notice}\n╚══════════════════╝\n"

        return f"""{notice_box}🎓 *CLASS {class_num} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━━━
📅 *WEEKLY TIME TABLE*
👇 Click to View
🔗 {t_link}

📝 *EXAM SCHEDULE (PDF)*
👇 Click to View
🔗 {e_link}

⏰ *TIMING DETAILS*
━━━━━━━━━━━━━━━━━━━
📍 *Tution:* 04:00 PM - 07:00 PM
✍️ *Exam:* *12:30 PM - 03:30 PM* ⚡
━━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

    # 🟡 2. INFO WORDS BINA NUMBER KE
    elif any(word in msg_lower for word in info_words):
        return "❓ *Kaunsi class ka?*\n\nApni class ka number likhein taaki main aapko sahi detail de sakun.\n\n👉 *Example: 10*"

    # 🟠 3. MAIN MENU (List Format)
    elif any(word in msg_lower for word in greet_words):
        global_msg = current_notices.get('all', "Sab normal")
        global_box = ""
        if "Sab normal" not in global_msg:
            global_box = f"╔══════════════════╗\n🚨  *URGENT NOTICE* 🚨\n\n  {global_msg}\n╚══════════════════╝\n"

        return f"""{global_box}🏛️ *PRINCE ACADEMY* 🏛️
━━━━━━━━━━━━━━━━━━━
👋 *Namaste!*

Apni Class ka number likhein:

6️⃣  *Class 6*
7️⃣  *Class 7*
8️⃣  *Class 8*
9️⃣  *Class 9*
🔟  *Class 10*
1️⃣1️⃣ *Class 11*
1️⃣2️⃣ *Class 12*

👇 *Jaise aise likhein:*
👉 *10*
👉 *Fees*
━━━━━━━━━━━━━━━━━━━"""

    # 🔵 4. PAYMENT
    elif any(word in msg_lower for word in pay_words):
        return f"💳 *FEES & PAYMENT*\n━━━━━━━━━━━━━━━━━━━\nUPI ID: *{PHONE_NO}@upi*\nNumber: *{PHONE_NO}*\n\n⚠️ Screenshot bhejna zaruri hai!\n━━━━━━━━━━━━━━━━━━━"

    elif 'wake' in msg_lower:
        return "I am awake!"

    # ⚪ 5. DEFAULT
    else:
        return "🤖 *Samajh nahi aaya!*\n\nKripya apni *Class ka number* (6-12) likhein ya *'Hi'* likhkar menu dekhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
