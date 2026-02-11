import os
from flask import Flask, request

app = Flask(__name__)

# --- 🏫 CONFIGURATION ---
INSTITUTE_NAME = "🎓 PRINCE CLASSES"
ADMISSION_CONTACT = "📞 9876543210 (Prince Sir)"

# --- 🧠 MAX KEYWORDS (Bot ka dimaag) ---
KEYWORDS = {
    'hello': ['hi', 'hello', 'hey', 'start', 'namaste', 'shuru', 'hlw', 'prince', 'sir', 'online', 'bot'],
    'time': ['time', 'tym', 'tiem', 'schedule', 'routine', 'kab', 'timing', 'lecture', 'period', 'table', 'ghadi', 'vakt'],
    'exam': ['exam', 'test', 'paper', 'pariksha', 'result', 'marks', 'date sheet', 'syllabus', 'viva', 'test plan'],
    'admission': ['admission', 'join', 'new', 'naya', 'enquiry', 'inquiry', 'office', 'contact', 'admission process'],
    'fee': ['fee', 'fees', 'paise', 'money', 'payment', 'khatam', 'dues']
}

def get_image_link(text):
    clean_text = text.replace(" ", "+")
    return f"https://placehold.co/600x800/png?text={clean_text}&font=roboto"

@app.route('/')
def home():
    return "🦁 Prince Classes Bot is Running Non-Stop!"

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    incoming_msg = request.args.get('msg', '').lower().strip()
    
    # 1. Class Check (6 to 12)
    detected_class = None
    for num in ['6', '7', '8', '9', '10', '11', '12']:
        if num in incoming_msg:
            detected_class = num
            break

    # 2. Keyword Check
    topic = None
    for key, word_list in KEYWORDS.items():
        if any(word in incoming_msg for word in word_list):
            topic = key
            break

    # 3. Decision Logic
    if topic == 'hello':
        return (f"👋 Namaste! Welcome to *{INSTITUTE_NAME}*.\n\n"
                "Mai aapka digital sahayak hu. 🤖\n"
                "Aapko kis class ki jankari chahiye?\n"
                "*(Example: Class 10 ya Time 11 likhein)*\n\n"
                "📌 Humare paas Class 6 se 12 tak ki coaching available hai.")

    elif topic == 'admission':
        return (f"🏛️ *Admission Helpline*\n\n"
                "Naye admission ke liye niche diye number par call karein ya office aayein:\n"
                f"{ADMISSION_CONTACT}\n"
                "📍 *Address:* Prince Classes, Main Road, Adajan, Surat.")

    elif detected_class:
        if topic == 'time':
            link = get_image_link(f"Class+{detected_class}+Time+Table")
            return f"📅 *Class {detected_class} Time Table:*\nDownload Link: {link}"
        elif topic == 'exam':
            link = get_image_link(f"Class+{detected_class}+Exam+Schedule")
            return f"📝 *Class {detected_class} Exam Dates:*\nCheck here: {link}"
        else:
            return (f"📂 *Class {detected_class} Information*\n\n"
                    f"Aap kya dekhna chahte hain?\n"
                    f"👉 *Time {detected_class}* (Schedule ke liye)\n"
                    f"👉 *Exam {detected_class}* (Exam plan ke liye)")

    # 4. Fallback (Jab kuch samajh na aaye)
    else:
        return ("⚠️ *Maaf karein, mujhe samajh nahi aaya.*\n\n"
                "Kripya niche diye gaye tareeke se reply karein:\n"
                "✅ *Hi* (Menu dekhne ke liye)\n"
                "✅ *Time 10* (Schedule ke liye)\n"
                "✅ *Admission* (Naye admission ke liye)")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
