from flask import Flask, request
import re  # Ye advanced tool hai jo number dhoondhta hai

app = Flask(__name__)

# ---------------------------------------------------------
# 👇 ADMIN SETTINGS (Yahan apne links aur number dalein)
# ---------------------------------------------------------

PHONE_NO = "9898308806"

# LINKS DICTIONARY (Apni Google Drive links yahan dalein)
TIMETABLE_LINKS = {
    '6':  "https://bit.ly/Prince-Class6",
    '7':  "https://bit.ly/Prince-Class7",
    '8':  "https://bit.ly/Prince-Class8",
    '9':  "https://bit.ly/Prince-Class9",
    '10': "https://bit.ly/Prince-Class10",
    '11': "https://bit.ly/Prince-Class11",
    '12': "https://bit.ly/Prince-Class12"
}

# DEFAULT NOTICES (Automatic Messages)
current_notices = {
    'all': "Sab normal", 
    '6':   "Sab normal",
    '7':   "Sab normal",
    '8':   "Sab normal",
    '9':   "Sab normal",
    '10':  "Sab normal",
    '11':  "Sab normal",
    '12':  "Sab normal"
}

# ---------------------------------------------------------

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    # Message ko saaf karenge
    msg = request.args.get('msg', '').strip()
    
    # --- 👑 ADMIN COMMAND (TEACHER ONLY) ---
    # Format: "set notice 10 Kal Test Hai"
    if msg.lower().startswith("set notice"):
        try:
            parts = msg.split(" ", 3) 
            if len(parts) < 4:
                return "❌ *Error:* Format galat hai.\nLikhein: *set notice 10 Message*"
                
            target = parts[2].lower()  # 'all' ya '10'
            new_notice = parts[3]      # Asli message

            if target in current_notices:
                current_notices[target] = new_notice
                return f"✅ *Success!*\n\nTarget: *{target.upper()}*\nNotice: *{new_notice}*\n\n(Update ho gaya!)"
            else:
                return "❌ *Error:* Class number 6 se 12 hi dalein ya 'all' likhein."
        except:
            return "❌ *Error:* Kuch gadbad hui."

    # --- 🤖 STUDENT LOGIC (Spelling Mistake Proof) ---

    msg_lower = msg.lower()
    
    # 1. SPELLING MISTAKE LISTS (Typos handle karne ke liye)
    # Agar baccha inme se kuch bhi likhega, bot samajh jayega
    greet_words = ['hi', 'hello', 'hey', 'helo', 'hy', 'hii', 'namaste', 'menu', 'start', 'shuru']
    
    class_words = ['class', 'classes', 'clas', 'clss', 'cls', 'kaksha', 'std', 'standard', 'batch',,'6','7','8','9'.'10','11','12', 'padhai']
    
    pay_words   = ['payment', 'pay', 'fee', 'fees', 'fess', 'feee', 'paisa', 'money', 'bank', 'qr', 'upi']
    
    query_words = ['query', 'quary', 'qury', 'qry', 'help', 'info', 'admission', 'addmission', 'office', 'time', 'address']

    # 2. SMART CLASS DETECTION (Regex Magic) 🧠
    # Ye 'class10', 'std 10', '10th', '10' sab mein se number nikal lega
    numbers_found = re.findall(r'\d+', msg_lower)
    
    # Check karenge ki kya number 6 se 12 ke beech hai?
    valid_class = None
    if numbers_found:
        for num in numbers_found:
            if num in ['6', '7', '8', '9', '10', '11', '12']:
                valid_class = num
                break

    if valid_class:
        class_num = valid_class
        final_link = TIMETABLE_LINKS.get(class_num, "Link jald aayega.")
        active_notice = current_notices.get(class_num, "Sab normal")
        
        # BOX LOGIC
        notice_box = ""
        if "Sab normal" not in active_notice:
            notice_box = f"""
╔══════════════════╗
📢  *CLASS {class_num} NOTICE*
  
  {active_notice}
╚══════════════════╝
"""
        return f"""{notice_box}🎓 *CLASS {class_num} DASHBOARD* 🎓
━━━━━━━━━━━━━━━━━━
📄 *TIME TABLE & LINKS:*
Link par click karein 👇
🔗 {final_link}

━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi,hello ,hii,menu,start' likhein*"""

    # 3. MAIN MENU (Jab baccha 'Hi', 'Hii', 'Helo' kare)
    elif any(word in msg_lower for word in greet_words):
        
        # Check GLOBAL notice ('all')
        global_msg = current_notices.get('all', "Sab normal")
        
        # BOX LOGIC for Global Notice
        global_box = ""
        if "Sab normal" not in global_msg:
            global_box = f"""
╔══════════════════╗
🚨  *URGENT NOTICE* 🚨
  
  {global_msg}
╚══════════════════╝
"""

        return f"""{global_box}🏛️ *PRINCE ACADEMY* 🏛️
━━━━━━━━━━━━━━━━━━
👋 *Namaste!*

Apni Class ka number likhein:
*(Time Table aur Notice dekhne ke liye)*

6️⃣  *Class 6*
7️⃣  *Class 7*
8️⃣  *Class 8*
9️⃣  *Class 9*
🔟  *Class 10*
1️⃣1️⃣ *Class 11*
1️⃣2️⃣ *Class 12*

👇 *Bas number likhein:*
👉 *10* ya *Class 12*
━━━━━━━━━━━━━━━━━━"""

    # 4. PAYMENT & FEES (Mistakes: 'fess', 'paymnt')
    elif any(word in msg_lower for word in pay_words):
        return f"""💳 *FEES & PAYMENT* 💳
━━━━━━━━━━━━━━━━━━
Aap fees is number par bhejein:

📱 *Google Pay / PhonePe:*
Number: *{PHONE_NO}*

🏦 *UPI ID:*
*{PHONE_NO}@upi*

⚠️ *Note:* Payment ka screenshot bhejna zaruri hai!
━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

    # 5. QUERY / ADMISSION (Mistakes: 'quary', 'addmission')
    elif any(word in msg_lower for word in query_words):
         return f"""❓ *OFFICE & HELP* ❓
━━━━━━━━━━━━━━━━━━
⏰ *Timing:*
Subah 10:00 se Shaam 08:00 tak.

📞 *Contact:*
Sir: *{PHONE_NO}*

📍 *Address:*
Prince Academy Tuition Center.
━━━━━━━━━━━━━━━━━━
🔙 *Menu ke liye 'Hi' likhein*"""

    # 6. WAKE UP
    elif 'wake' in msg_lower:
        return "I am awake!"

    # 7. DEFAULT
    else:
        return """🤖 *Samajh nahi aaya!*
━━━━━━━━━━━━━━━━━━
✨Bas apni class ka number likhein.

Jaise:
👉 *10*
👉 *Class 12*
👉 *Fees*"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
