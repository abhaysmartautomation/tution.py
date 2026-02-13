from flask import Flask, request
import re
import traceback

app = Flask(__name__)

# =========================================================
# ⚙️ ADMIN SETTINGS (ABHAY TUITION SPECIAL)
# =========================================================
FORM_LINK = "https://forms.gle/GWipzdU8hbPxZF6dA"
PHONE_NO  = "9898308806"
WA_LINK   = f"https://wa.me/91{PHONE_NO}" 
MAP_LINK  = "http://maps.google.com/?q=Prince+Academy+Surat"

# Result Data (Subject Wise)
STUDENT_RESULTS = {
    '101': '*Rahul Kumar (Class 10)*\n📐 Maths: 95\n🔬 Science: 90\n📖 English: 85\n📊 *Percentage: 90%*',
    '102': '*Sneha Gupta (Commerce)*\n💰 Accounts: 82\n📈 Economics: 88\n📝 B.St: 85\n📊 *Percentage: 85%*',
    '103': '*Amit Sharma (Science)*\n⚛️ Physics: 72\n🧪 Chemistry: 68\n📐 Maths: 76\n📊 *Percentage: 72%*'
}

# Timetable & Links (6 to 12)
TIMETABLE_LINKS = {str(i): f"https://bit.ly/Abhay-Class{i}" for i in range(6, 13)}
EXAM_LINKS      = {str(i): f"https://bit.ly/Exam-Class{i}" for i in range(6, 13)}

# Notices (Memory)
current_notices = {str(i): "Sab normal" for i in range(6, 13)}
current_notices['all'] = "Sab normal"

# =========================================================
# 🛡️ SMART SPELLING & ERROR PROTECTION LOGIC
# =========================================================

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    try:
        raw_msg = request.args.get('msg', '')
        
        # 🚨 EMPTY MESSAGE FIX (Agar kuch na likha ho)
        if not raw_msg or not raw_msg.strip():
            return main_menu(current_notices.get('all', "Sab normal"))

        msg = raw_msg.strip()
        msg_lower = msg.lower()

        # 🛠️ ADMIN COMMAND (Notice Setting)
        if msg_lower.startswith("set notice"):
            parts = msg.split(" ", 3)
            if len(parts) >= 4:
                target = parts[2].lower()
                current_notices[target] = parts[3]
                return f"✅ Notice Updated for {target.upper()}!"

        # 🧠 RELATABLE SPELLING PATTERNS (Typos Proof)
        # Leave patterns (Chutti, Bimar, Application, etc.)
        leave_pattern  = r"(leave|chutti|chuti|chuty|absent|absnt|bimar|sick|aplication|aply|leav|bukhar|chhuti)"
        
        # Result patterns (Marks, Score, Number, Roll, etc.)
        result_pattern = r"(result|reslt|rsult|marks|score|nambar|number|mark|roll|rol|no|resut)"
        
        # Help/Admission patterns (Fees, Query, Info, Contact, etc.)
        query_pattern  = r"(query|help|admi|addmi|fees|pay|locat|paisa|contact|address|adrss|form|detal|info|pese|admission)"
        
        # Greeting patterns
        greet_pattern  = r"^(hi|hello|helo|hii|hey|menu|start|namaste|hy|hlo|hey|yo|abhay|tution|tuition)$"

        # Safe Number Finder (Class/Roll No dhoondne ke liye)
        found_numbers = re.findall(r'\d+', msg_lower)
        valid_class = next((n for n in found_numbers if n in TIMETABLE_LINKS), None)

        # =====================================================
        # 👇 BRANCHING LOGIC
        # =====================================================

        # --- 1. LEAVE BRANCH ---
        if re.search(leave_pattern, msg_lower):
            return f"""🤒 *LEAVE APPLICATION*
━━━━━━━━━━━━━━━━━━━
Aap aaj class nahi aa rahe? 

Niche diye gaye link par form bharein. Sir ko turant update mil jayega.

👉 *CLICK TO FILL:*
🔗 {FORM_LINK}
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 2. RESULT BRANCH ---
        elif re.search(result_pattern, msg_lower):
            if found_numbers:
                roll = found_numbers[0]
                if roll in STUDENT_RESULTS:
                    return f"📊 *EXAM RESULT*\n━━━━━━━━━━━━━━━━━━━\n🆔 *Roll:* {roll}\n{STUDENT_RESULTS[roll]}\n━━━━━━━━━━━━━━━━━━━\n🏆 *All the Best!*"
                else:
                    return f"❌ *Record Nahi Mila!* \nRoll No *{roll}* sahi se check karein."
            else:
                return "❓ *Roll No likhein!* \nResult dekhne ke liye Roll No likhein. \n👉 Ex: *Result 101*"

        # --- 3. HELP & QUERY BRANCH ---
        elif re.search(query_pattern, msg_lower):
            return f"""🏛️ *ABHAY TUITION HELP* 🏛️
━━━━━━━━━━━━━━━━━━━
📝 *ADMISSION:* https://bit.ly/Form
💳 *FEES (UPI):* {PHONE_NO}@upi
📞 *CONTACT SIR:* {WA_LINK}
📍 *LOCATION:* {MAP_LINK}
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 4. CLASS DASHBOARD (Old Style) ---
        elif valid_class:
            cls = valid_class
            notice = current_notices.get(cls, "Sab normal")
            n_box = ""
            if "Sab normal" not in notice:
                n_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {notice.upper()}\n╚══════════════════╝\n"
            
            return f"""{n_box}🎓 *CLASS {cls} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━━━
📅 *WEEKLY TIME TABLE*
👇 Click to View
🔗 {TIMETABLE_LINKS[cls]}

📝 *EXAM SCHEDULE (PDF)*
👇 Click to View
🔗 {EXAM_LINKS[cls]}

⏰ *TIMING DETAILS*
━━━━━━━━━━━━━━━━━━━
📍 *Classes:* 04:00 PM - 07:00 PM
✍️ *Exam:* *12:30 PM - 03:30 PM* ⚡
━━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

        # --- 5. MAIN MENU (Default Response) ---
        else:
            return main_menu(current_notices.get('all', "Sab normal"))

    except Exception:
        # Emergency safety (Error hone par Menu dikhao)
        return main_menu(current_notices.get('all', "Sab normal"))

# 🏛️ Function: Main Menu (Abhay Tuition Style)
def main_menu(g_msg):
    g_box = ""
    if "Sab normal" not in g_msg:
        g_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {g_msg.upper()}\n╚══════════════════╝\n"
    
    return f"""{g_box}🏛️ *ABHAY TUITION CLASSES* 🏛️
━━━━━━━━━━━━━━━━━━━
👋 *Namaste!*

👇 *Apna Option Chuniye:*

6️⃣  *Class 6*
7️⃣  *Class 7*
8️⃣  *Class 8*
9️⃣  *Class 9*
🔟  *Class 10*
1️⃣1️⃣ *Class 11*
1️⃣2️⃣ *Class 12*

🟡 *Query / Admission*
🟡 *Check Result*
🟡 *Leave Application*

━━━━━━━━━━━━━━━━━━━"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
