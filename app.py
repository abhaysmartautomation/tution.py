from flask import Flask, request
import re

app = Flask(__name__)

# =========================================================
# ⚙️ ADMIN & LINK SETTINGS
# =========================================================

# 👇 AAPKA FORM LINK (Yahan Paste Karein)
FORM_LINK = "https://forms.gle/GWipzdU8hbPxZF6dA"

PHONE_NO  = "9898308806"
WA_LINK   = f"https://wa.me/91{PHONE_NO}" 
MAP_LINK  = "http://maps.google.com/?q=Prince+Academy+Surat"

# 📊 RESULT DATA (Smart Subject Wise)
STUDENT_RESULTS = {
    '101': '*Rahul Kumar (Class 10)*\n📐 Maths: 95\n🔬 Science: 90\n📖 English: 85\n📊 *Percentage: 90%*',
    '102': '*Sneha Gupta (Commerce)*\n💰 Accounts: 82\n📈 Economics: 88\n📝 B.St: 85\n📊 *Percentage: 85%*',
    '103': '*Amit Sharma (Science)*\n⚛️ Physics: 72\n🧪 Chemistry: 68\n📐 Maths: 76\n📊 *Percentage: 72%*'
}

# 🔗 CLASS LINKS
TIMETABLE_LINKS = {str(i): f"https://bit.ly/Prince-Class{i}" for i in range(6, 13)}
EXAM_LINKS      = {str(i): f"https://bit.ly/Exam-Class{i}" for i in range(6, 13)}

# 📢 NOTICE BOARD (Memory)
current_notices = {str(i): "Sab normal" for i in range(6, 13)}
current_notices['all'] = "Sab normal"

# =========================================================
# 🚀 MAIN LOGIC
# =========================================================

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    msg = request.args.get('msg', '')
    if not msg: return ""
    
    msg = msg.strip()
    msg_lower = msg.lower()

    # --- 0. ADMIN COMMAND (Sir ke liye) ---
    # Format: set notice all Kal Chutti Hai
    if msg_lower.startswith("set notice"):
        try:
            parts = msg.split(" ", 3)
            target = parts[2].lower() # 'all' ya '10'
            note_text = parts[3]
            if target in current_notices or target == 'all':
                current_notices[target] = note_text
                return f"✅ Notice Set Successfully for {target.upper()}!"
        except: return "❌ Error! Format: set notice all [Message]"

    # --- 1. SPELLING MISTAKE PATTERNS (Fuzzy Logic) ---
    # Ye galat spelling ko bhi pakad lega
    query_pattern  = r"(query|qery|queri|admi|addmi|help|sahayta|form|fees|pay|locat|paisa|contact)"
    result_pattern = r"(result|reslt|rsult|marks|score|nambar|number|mark)"
    leave_pattern  = r"(leave|chutti|absent|nahi aaunga|bimar|sick|application|leav|chuti|bukhar)"
    greet_pattern  = r"^(hi|hello|helo|hii|hey|menu|start|namaste|hy|hlo)$"

    # --- 2. NUMBER FINDER ---
    found_numbers = re.findall(r'\d+', msg_lower)
    valid_class = next((n for n in found_numbers if n in TIMETABLE_LINKS), None)

    # =====================================================
    # 👇 RESPONSE LOGIC
    # =====================================================

    # 🤒 BRANCH 1: LEAVE APPLICATION
    if re.search(leave_pattern, msg_lower):
        return f"""🤒 *LEAVE APPLICATION*
━━━━━━━━━━━━━━━━━━━
Aap aaj class nahi aa rahe👍? 

Niche diye gaye link par form bharein. Sir ke paas turant update pahunch jayega.

👉 *CLICK TO FILL:*
🔗 {FORM_LINK}

*Note:* Jhoot bolne par Sir call karenge! 📞
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

    # 📊 BRANCH 2: RESULT CHECKER
    elif re.search(result_pattern, msg_lower):
        if found_numbers and found_numbers[0] in STUDENT_RESULTS:
            roll = found_numbers[0]
            return f"""📊 *EXAM RESULT DECLARATION*
━━━━━━━━━━━━━━━━━━━
🆔 *Roll No:* {roll}
👤 *Student Detail:*
{STUDENT_RESULTS[roll]}
━━━━━━━━━━━━━━━━━━━
🏆 *Keep it up!*
🏠 *Menu ke liye 'Hi' likhein*"""
        else:
            return "❌ *Result nahi mila!* \nSahi Roll No likhein. \n👉 Example: *Result 101*"

    # 🏛️ BRANCH 3: HELP & ADMISSION
    elif re.search(query_pattern, msg_lower):
        return f"""🏛️ *HELP & ADMISSION DESK* 🏛️
━━━━━━━━━━━━━━━━━━━
📝 *NEW ADMISSION FORM*
🔗 https://bit.ly/Prince-Admission-Form

💳 *FEES PAYMENT (UPI)*
🔗 {PHONE_NO}@upi

📞 *CONTACT SIR*
🔗 {WA_LINK}

📍 *LOCATION*
🔗 {MAP_LINK}
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

    # 🎓 BRANCH 4: CLASS DASHBOARD (With RED NOTICE)
    elif valid_class:
        cls = valid_class
        notice = current_notices.get(cls, "Sab normal")
        
        # 🚨 Notice Box Logic (Agar notice hai to Red Box dikhega)
        notice_box = ""
        if "Sab normal" not in notice:
            notice_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {notice.upper()}\n╚══════════════════╝\n"

        return f"""{notice_box}🎓 *CLASS {cls} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━━━
📅 *WEEKLY TIME TABLE*
👇 Click to View
🔗 {TIMETABLE_LINKS[cls]}

📝 *EXAM SCHEDULE (PDF)*
👇 Click to View
🔗 {EXAM_LINKS[cls]}

⏰ *TIMING DETAILS*
━━━━━━━━━━━━━━━━━━━
📍 *Tution:* 04:00 PM - 07:00 PM
✍️ *Exam:* *12:30 PM - 03:30 PM* ⚡
━━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

    # 👋 BRANCH 5: MAIN MENU (With RED NOTICE)
    elif re.search(greet_pattern, msg_lower):
        
        # 🚨 Global Notice Box Logic
        g_msg = current_notices.get('all', "Sab normal")
        g_box = ""
        if "Sab normal" not in g_msg:
             g_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {g_msg.upper()}\n╚══════════════════╝\n"

        return f"""{g_box}🏛️ *PRINCE ACADEMY* 🏛️
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

    # 🤖 BRANCH 6: DEFAULT
    else:
        return "🤖 *Samajh nahi aaya!*\n\nClass Number (6-12) likhein, *Result* likhein ya *Query* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
