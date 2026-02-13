from flask import Flask, request
import re

app = Flask(__name__)

# =========================================================
# ⚙️ ADMIN SETTINGS
# =========================================================
PHONE_NO  = "9898308806"
WA_LINK   = f"https://wa.me/91{PHONE_NO}" 
YT_LINK   = "https://youtube.com/c/PrinceAcademy"
FORM_LINK = "https://bit.ly/Prince-Admission-Form"
MAP_LINK  = "http://maps.google.com/?q=Prince+Academy+Surat"

# 📊 SMART RESULT DATA (Ab Subject-wise aur Percentage ke sath)
STUDENT_RESULTS = {
    '101': '*Rahul Kumar (Class 10)*\n📐 Maths: 95\n🔬 Science: 90\n📖 English: 85\n📊 *Percentage: 90%*',
    
    '102': '*Sneha Gupta (Commerce)*\n💰 Accounts: 82\n📈 Economics: 88\n📝 B.St: 85\n📊 *Percentage: 85%*',
    
    '103': '*Amit Sharma (Science)*\n⚛️ Physics: 72\n🧪 Chemistry: 68\n📐 Maths: 76\n📊 *Percentage: 72%*'
}

# 🔗 CLASS LINKS
TIMETABLE_LINKS = {str(i): f"https://bit.ly/Prince-Class{i}" for i in range(6, 13)}
EXAM_LINKS      = {str(i): f"https://bit.ly/Exam-Class{i}" for i in range(6, 13)}

# 📢 NOTICES
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

    # --- FUZZY KEYWORDS (Spelling mistake proof) ---
    query_pattern = r"(query|qery|queri|admi|addmi|help|sahayta|form|fees|pay|locat|paisa)"
    result_pattern = r"(result|reslt|rsult|marks|score|nambar|number)"
    greet_pattern = r"^(hi|hello|helo|hii|hey|menu|start|namaste|hy)$"

    # --- NUMBER FINDER ---
    found_numbers = re.findall(r'\d+', msg_lower)
    valid_class = next((n for n in found_numbers if n in TIMETABLE_LINKS), None)

    # 🟢 1. CLASS DASHBOARD
    if valid_class:
        cls = valid_class
        notice = current_notices.get(cls, "Sab normal")
        n_box = f"╔══════════════════╗\n📢  *CLASS {cls} NOTICE*\n\n  {notice}\n╚══════════════════╝\n" if "Sab normal" not in notice else ""

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
📍 *Tution:* 04:00 PM - 07:00 PM
✍️ *Exam:* *12:30 PM - 03:30 PM* ⚡
━━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

    # 🟣 2. HELP & ADMISSION (Full Details)
    elif re.search(query_pattern, msg_lower):
        return f"""🏛️ *HELP & ADMISSION DESK* 🏛️
━━━━━━━━━━━━━━━━━━━
📝 *NEW ADMISSION FORM*
🔗 {FORM_LINK}

💳 *FEES PAYMENT (UPI)*
🔗 {PHONE_NO}@upi

📞 *CONTACT SIR*
🔗 {WA_LINK}

📍 *LOCATION*
🔗 {MAP_LINK}
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

    # 🆕 3. SMART RESULT CHECKER (Fixed & Detailed)
    elif re.search(result_pattern, msg_lower):
        roll = found_numbers[0] if found_numbers else None
        if roll in STUDENT_RESULTS:
            return f"""📊 *EXAM RESULT DECLARATION*
━━━━━━━━━━━━━━━━━━━
🆔 *Roll No:* {roll}
👤 *Student Detail:*
{STUDENT_RESULTS[roll]}
━━━━━━━━━━━━━━━━━━━
🏆 *Keep it up!*
🏠 *Menu ke liye 'Hi' likhein*"""
        else:
            return "❌ *Result nahi mila!* \nApna Roll No likhein. \n👉 Example: *Result 101*"

    # 🟠 4. MAIN MENU (Vertical List with Yellow Dots)
    elif re.search(greet_pattern, msg_lower):
        g_msg = current_notices.get('all', "Sab normal")
        g_box = f"╔══════════════════╗\n🚨  *URGENT NOTICE* 🚨\n\n  {g_msg}\n╚══════════════════╝\n" if "Sab normal" not in g_msg else ""

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

━━━━━━━━━━━━━━━━━━━"""

    # 🔵 5. DEFAULT
    else:
        return "🤖 *Samajh nahi aaya!*\n\nClass Number (6-12) likhein ya *Query* likhein."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
