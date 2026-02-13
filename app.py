from flask import Flask, request
import re
import traceback # Error detail check karne ke liye

app = Flask(__name__)

# =========================================================
# ⚙️ ADMIN SETTINGS (Aapka Data)
# =========================================================
FORM_LINK = "https://forms.gle/GWipzdU8hbPxZF6dA"
PHONE_NO  = "9898308806"
WA_LINK   = f"https://wa.me/91{PHONE_NO}" 
MAP_LINK  = "http://maps.google.com/?q=Prince+Academy+Surat"

STUDENT_RESULTS = {
    '101': '*Rahul Kumar (Class 10)*\n📐 Maths: 95\n🔬 Science: 90\n📖 English: 85\n📊 *Percentage: 90%*',
    '102': '*Sneha Gupta (Commerce)*\n💰 Accounts: 82\n📈 Economics: 88\n📝 B.St: 85\n📊 *Percentage: 85%*',
    '103': '*Amit Sharma (Science)*\n⚛️ Physics: 72\n🧪 Chemistry: 68\n📐 Maths: 76\n📊 *Percentage: 72%*'
}

TIMETABLE_LINKS = {str(i): f"https://bit.ly/Prince-Class{i}" for i in range(6, 13)}
EXAM_LINKS      = {str(i): f"https://bit.ly/Exam-Class{i}" for i in range(6, 13)}
current_notices = {str(i): "Sab normal" for i in range(6, 13)}
current_notices['all'] = "Sab normal"

# =========================================================
# 🚀 SECURE LOGIC
# =========================================================

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    try:
        msg = request.args.get('msg', '')
        if not msg: return ""
        
        msg = msg.strip()
        msg_lower = msg.lower()

        # --- Admin Notice Control ---
        if msg_lower.startswith("set notice"):
            parts = msg.split(" ", 3)
            if len(parts) >= 4:
                target = parts[2].lower()
                current_notices[target] = parts[3]
                return f"✅ Notice Updated for {target.upper()}!"

        # --- Keywords & Fuzzy Logic ---
        query_pattern  = r"(query|qery|queri|admi|addmi|help|sahayta|form|fees|pay|locat|paisa|contact)"
        result_pattern = r"(result|reslt|rsult|marks|score|nambar|number|mark)"
        leave_pattern  = r"(leave|chutti|absent|nahi aaunga|bimar|sick|application|leav|chuti)"
        greet_pattern  = r"^(hi|hello|helo|hii|hey|menu|start|namaste|hy|hlo)$"

        # --- Safe Number Finding ---
        found_numbers = re.findall(r'\d+', msg_lower)
        valid_class = next((n for n in found_numbers if n in TIMETABLE_LINKS), None)

        # 🤒 1. LEAVE BRANCH
        if re.search(leave_pattern, msg_lower):
            return f"""🤒 *LEAVE APPLICATION*
━━━━━━━━━━━━━━━━━━━
Aap aaj class nahi aa rahe? 

Niche diye gaye link par form bharein. Sir ko turant update mil jayega.

👉 *CLICK TO FILL:*
🔗 {FORM_LINK}

*Note:* Sabhi information sahi bharein.
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # 📊 2. RESULT BRANCH (Safe access)
        elif re.search(result_pattern, msg_lower):
            if found_numbers:
                roll = found_numbers[0]
                if roll in STUDENT_RESULTS:
                    return f"""📊 *EXAM RESULT*
━━━━━━━━━━━━━━━━━━━
🆔 *Roll No:* {roll}
{STUDENT_RESULTS[roll]}
━━━━━━━━━━━━━━━━━━━
🏆 *Keep it up!*"""
                else:
                    return f"❌ *Roll No {roll}* ka result nahi mila. Kripya sahi ID dalein."
            else:
                return "❓ *Roll No missing!* \nResult dekhne ke liye Roll No bhi likhein.\n👉 Example: *Result 101*"

        # 🏛️ 3. QUERY BRANCH
        elif re.search(query_pattern, msg_lower):
            return f"""🏛️ *HELP & ADMISSION* 🏛️
━━━━━━━━━━━━━━━━━━━
📝 *ADMISSION FORM:* https://bit.ly/Form
💳 *FEES (UPI):* {PHONE_NO}@upi
📞 *CONTACT:* {WA_LINK}
📍 *LOCATION:* {MAP_LINK}
━━━━━━━━━━━━━━━━━━━"""

        # 🎓 4. CLASS DASHBOARD
        elif valid_class:
            cls = valid_class
            notice = current_notices.get(cls, "Sab normal")
            n_box = ""
            if "Sab normal" not in notice:
                n_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {notice.upper()}\n╚══════════════════╝\n"

            return f"""{n_box}🎓 *CLASS {cls} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━━━
📅 *TIME TABLE:* {TIMETABLE_LINKS[cls]}
📝 *EXAM SCH:* {EXAM_LINKS[cls]}
━━━━━━━━━━━━━━━━━━━
📍 *Tution:* 04:00 PM - 07:00 PM
🔙 *Menu ke liye 'Hi' likhein*"""

        # 👋 5. MAIN MENU
        elif re.search(greet_pattern, msg_lower):
            g_msg = current_notices.get('all', "Sab normal")
            g_box = ""
            if "Sab normal" not in g_msg:
                g_box = f"🚨🔴 *URGENT NOTICE* 🔴🚨\n╔══════════════════╗\n  👉 {g_msg.upper()}\n╚══════════════════╝\n"

            return f"""{g_box}🏛️ *PRINCE ACADEMY* 🏛️
━━━━━━━━━━━━━━━━━━━
👋 *Namaste!*

👇 *Option Type Karein:*

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

        # 🤖 6. DEFAULT
        else:
            return "🤖 *Samajh nahi aaya!*\n\nClass Number (6-12) likhein, *Result* likhein ya *Query* likhein."

    except Exception as e:
        print(f"CRITICAL ERROR: {traceback.format_exc()}")
        return "⚠️ *System Busy:* Kripya 1 minute baad koshish karein. Hum ise theek kar rahe hain."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
