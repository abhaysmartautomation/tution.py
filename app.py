from flask import Flask, request
import re

app = Flask(__name__)

# =========================================================
# ⚙️ ADMIN SETTINGS
# =========================================================
FORM_LINK = "https://forms.gle/GWipzdU8hbPxZF6dA"
PHONE_NO  = "9898308806"
WA_LINK   = f"https://wa.me/91{PHONE_NO}" 
MAP_LINK  = "http://maps.google.com/?q=Prince+Academy+Surat"
UPI_ID    = f"{PHONE_NO}@upi"

# Result Data
STUDENT_RESULTS = {
    '101': '👤 *Rahul Kumar (Class 10)*\n📐 Maths: 95\n🔬 Science: 90\n📖 English: 85\n📊 *Percentage: 90%*',
    '102': '👤 *Sneha Gupta (Commerce)*\n💰 Accounts: 82\n📈 Economics: 88\n📝 B.St: 85\n📊 *Percentage: 85%*',
    '103': '👤 *Amit Sharma (Science)*\n⚛️ Physics: 72\n🧪 Chemistry: 68\n📐 Maths: 76\n📊 *Percentage: 72%*'
}

# Timetable & Links
TIMETABLE_LINKS = {str(i): f"https://bit.ly/Abhay-Class{i}" for i in range(6, 13)}
EXAM_LINKS      = {str(i): f"https://bit.ly/Exam-Class{i}" for i in range(6, 13)}

# Notices
current_notices = {str(i): "Sab normal" for i in range(6, 13)}
current_notices['all'] = "Sab normal"

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    try:
        raw_msg = request.args.get('msg', '')
        if not raw_msg or not raw_msg.strip():
            return main_menu(current_notices.get('all', "Sab normal"))

        msg = raw_msg.strip()
        msg_lower = msg.lower()

        # 🛠️ ADMIN COMMAND
        if msg_lower.startswith("set notice"):
            parts = msg.split(" ", 3)
            if len(parts) >= 4:
                target = parts[2].lower()
                current_notices[target] = parts[3]
                return f"✅ Notice Updated for {target.upper()}!"

        # 🧠 PATTERNS
        leave_pattern  = r"(leave|chutti|chuti|chuty|absent|absnt|bimar|sick|aplication|aply|leav|bukhar|chhuti)"
        result_pattern = r"(result|reslt|rsult|marks|score|nambar|number|mark|roll|rol|no|resut)"
        query_pattern  = r"(query|help|admi|addmi|fees|pay|locat|paisa|contact|address|adrss|form|detal|info|pese|admission)"
        
        found_numbers = re.findall(r'\d+', msg_lower)
        valid_class = next((n for n in found_numbers if n in TIMETABLE_LINKS), None)

        # =====================================================
        # 👇 BRANCHING LOGIC
        # =====================================================

        # --- 1. LEAVE DASHBOARD ---
        if re.search(leave_pattern, msg_lower):
            return f"""🤒 *LEAVE DASHBOARD*
━━━━━━━━━━━━━━━━━━━
⚠️ *Absent Today?*
Agar aap aaj class nahi aa pa rahe, to niche link par form bharein.

📝 *FILL APPLICATION:*
👇 Click Here
🔗 {FORM_LINK}

✅ *Status:* Sir will be notified.
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 2. RESULT DASHBOARD ---
        elif re.search(result_pattern, msg_lower):
            if found_numbers:
                roll = found_numbers[0]
                if roll in STUDENT_RESULTS:
                    return f"""🏆 *RESULT DASHBOARD*
━━━━━━━━━━━━━━━━━━━
🆔 *Roll No:* {roll}
{STUDENT_RESULTS[roll]}
━━━━━━━━━━━━━━━━━━━
🌟 *Keep Working Hard!*
🏠 *Menu ke liye 'Hi' likhein*"""
                else:
                    return f"""❌ *ERROR*
━━━━━━━━━━━━━━━━━━━
Roll No *{roll}* ka record nahi mila.
Kripya sahi number check karein.
━━━━━━━━━━━━━━━━━━━"""
            else:
                return f"""❓ *INPUT REQUIRED*
━━━━━━━━━━━━━━━━━━━
Result dekhne ke liye Roll No likhein.
👉 Example: *Result 101*
━━━━━━━━━━━━━━━━━━━"""

        # --- 3. HELP & QUERY DASHBOARD ---
        elif re.search(query_pattern, msg_lower):
            return f"""🤝 *HELP & SUPPORT*
━━━━━━━━━━━━━━━━━
📝 *ADMISSION FORM*
🔗 https://bit.ly/Form

💳 *FEES PAYMENT (UPI)*
🆔 {UPI_ID}

📍 *GOOGLE LOCATION*
🔗 {MAP_LINK}

📞 *CONTACT SIR*
🔗 {WA_LINK}
━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 4. CLASS DASHBOARD ---
        elif valid_class:
            cls = valid_class
            notice = current_notices.get(cls, "Sab normal")
            n_box = ""
            if "Sab normal" not in notice:
                n_box = f"🚨 *NOTICE:* {notice.upper()}\n━━━━━━━━━━━━━━━━━━━\n"
            
            return f"""🎓 *CLASS {cls} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━
{n_box}📅 *TIME TABLE*
👇 Click to View
🔗 {TIMETABLE_LINKS[cls]}

📝 *EXAM SCHEDULE*
👇 Click to Download
🔗 {EXAM_LINKS[cls]}

⏰ *TIMING:* 04:00 PM - 07:00 PM
━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 5. MAIN MENU ---
        else:
            return main_menu(current_notices.get('all', "Sab normal"))

    except Exception:
        return main_menu(current_notices.get('all', "Sab normal"))

# 🏛️ Function: Main Menu (OLD STYLE BACK ✅)
def main_menu(g_msg):
    n_box = ""
    if "Sab normal" not in g_msg:
        n_box = f"🚨 *NOTICE:* {g_msg.upper()}\n━━━━━━━━━━━━━━━━━━━\n"
    
    return f"""{n_box}🏛️ *ABHAY TUITION CLASSES* 🏛️
━━━━━━━━━━━━━━━━━━
👋 *Namaste! Welcome back✨.*
👇 *Apna Option Chuniye:*

6️⃣  *Class 6*
7️⃣  *Class 7*
8️⃣  *Class 8*
9️⃣  *Class 9*
🔟  *Class 10*
1️⃣1️⃣ *Class 11*
1️⃣2️⃣ *Class 12*

🟡 *QUERY*:- FOR DOUBT✨
🟡 *RESULT*:-FOR RESULT✨
🟡 *Application*:-FOR LEAVE REPORT✨

━━━━━━━━━━━━━━━━━━"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
