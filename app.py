import os
from flask import Flask, request

app = Flask(__name__)

# --- CONFIGURATION ---
HEADER = "🏛️ *PRINCE ACADEMY* 🏛️"
LINE = "━━━━━━━━━━━━━━━━━━━━"
FOOTER = f"\n{LINE}\n🏠 *Main Menu:* Type 'Hi'"

@app.route('/')
def home(): return "Prince Academy Pro System is Running! 🚀"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    raw_msg = request.args.get('msg', '')
    msg = raw_msg.replace('{', '').replace('}', '').lower().strip()

    # ==========================================
    # LEVEL 0: MAIN DASHBOARD (Aapka Edit Kiya Hua)
    # ==========================================
    if msg in ['hi','hii','chalu','he', 'hello', 'start', 'menu', 'namaste']:
        return (f"{HEADER}\n"
                f"Syllabus, Fees aur Results ke liye niche diye keywords type karein:\n\n"
                "📂 *CLASSES* - ✨Classes ki jankari ke liye✨\n"
                "💳 *PAYMENT* - 💲Fees aur Pay details💲\n"
                "📝 *ADMISSION* - ✨Naye dakhile ke liye✨\n"
                "📍 *OFFICE* -💖 Address aur officeTiming💖"
                f"{FOOTER}")

    # ==========================================
    # LEVEL 1: CLASSES SELECTION (Aapka Edit Kiya Hua)
    # ==========================================
    if msg == 'classes':
        return (f"{HEADER}\n"
                f"📑 *SELECT YOUR CLASS*\n{LINE}\n"
                "Kripya apni class ka number likhein:\n\n"
                "👉 *6️⃣🔸7️⃣🔸8️⃣🔸9️⃣🔸🔟🔸1️⃣1️⃣🔸1️⃣2️⃣*"
                f"{FOOTER}")

    # ==========================================
    # LEVEL 1: PAYMENT & FEES MENU
    # ==========================================
    if msg == 'payment':
        return (f"{HEADER}\n"
                f"💳 *FEES & PAYMENT CENTER*\n{LINE}\n"
                "Kripya option type karein:\n\n"
                "💰 *Structure* - Fees janne ke liye\n"
                "📲 *Pay Now* - Online payment link\n"
                "🧾 *Receipt* - Payment proof kaise bhejien"
                f"{FOOTER}")

    # ==========================================
    # LEVEL 2: CLASS SPECIFIC MENU
    # ==========================================
    classes = [str(i) for i in range(6, 13)]
    if msg in classes:
        return (f"{HEADER}\n"
                f"📂 *CLASS {msg} DASHBOARD*\n{LINE}\n"
                "Aap is class me kya dekhna chahte hain? Type karein:\n\n"
                f"🕒 *Time {msg}* - Time Table\n"
                f"🗓️ *Exam {msg}* - Exam Schedule\n"
                f"📞 *Support {msg}* - Teacher Contact"
                f"{FOOTER}")

    # ==========================================
    # LEVEL 3: FINAL DATA (PDF & LINK ADDED HERE)
    # ==========================================
    detected_class = next((c for c in classes if c in msg), None)
    
    if detected_class:
        # --- TIME TABLE SECTION ---
        if 'time' in msg:
            return (f"{HEADER}\n"
                    f"🕒 *TIME TABLE: CLASS {detected_class}*\n{LINE}\n"
                    "Ye raha aapka class time table PDF format me. 📥\n\n"
                    "📄 *Download PDF:* bit.ly/TimeTable_PDF_Link\n\n"
                    "Morning Batch: 08:00 AM\n"
                    "📍 Room No: 104"
                    f"\n\n🔙 *Back:* Type '{detected_class}'"
                    f"{FOOTER}")
        
        # --- EXAM SCHEDULE SECTION (Aapki Demand Par) ---
        elif 'exam' in msg:
            return (f"{HEADER}\n"
                    f"🗓️ *EXAM SCHEDULE: CLASS {detected_class}*\n{LINE}\n"
                    "Here is your exam schedule, Best of Luck! 🏆✨\n\n"
                    "📄 *PDF Link:* bit.ly/ExamSchedule_PDF_Link\n\n"
                    "• Finals: 15th March\n"
                    "• Timing: 10:00 AM to 01:00 PM"
                    f"\n\n🔙 *Back:* Type '{detected_class}'"
                    f"{FOOTER}")

        elif 'support' in msg:
            return (f"{HEADER}\n"
                    f"📞 *TEACHER CONTACT: CLASS {detected_class}*\n{LINE}\n"
                    "Sawaal puchne ke liye call karein:\n"
                    "👤 *In-charge:* Mr. Prince\n"
                    "📱 *Mobile:* 98X98308806"
                    f"\n\n🔙 *Back:* Type '{detected_class}'"
                    f"{FOOTER}")

    # ==========================================
    # SUB-LEVEL: PAYMENT DETAILS
    # ==========================================
    if msg == 'structure':
        return (f"{HEADER}\n"
                "💰 *MONTHLY FEES STRUCTURE*\n"
                "• 6th-8th: ₹1500\n• 9th-10th: ₹2000\n• 11th-12th: ₹2500"
                f"\n\n🔙 *Back:* Type 'payment'" + FOOTER)
    
    if msg == 'pay now':
        return (f"{HEADER}\n"
                "📲 *FAST PAYMENT*\n"
                "UPI ID: `prince@upi` (Tap to copy)\n"
                "Google Pay/PhonePe: Click bit.ly/PayPrince"
                f"\n\n🔙 *Back:* Type 'payment'" + FOOTER)

    if msg == 'office':
        return (f"{HEADER}\n"
                "📍 *OFFICE LOCATION*\n"
                "Prince Academy, Building No. 5, Near Station.\n"
                "⏰ 09:00 AM - 06:00 PM"
                f"{FOOTER}")

    # FALLBACK (Aapka customized fallback)
    return (f"{HEADER}\n"
            "⚠️ *Option Galat Hai!*\n\n"
            "Kripya main menu ke liye *'Hi'* likhein ye achhe se opt likhe 😉🧐."
            f"{FOOTER}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
