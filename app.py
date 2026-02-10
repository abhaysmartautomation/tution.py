import os
from flask import Flask, request

app = Flask(__name__)

# --- 1. SETTINGS (यहाँ अपना असली डाटा पेस्ट करें) ---

COACHING_NAME = "Uday Reloaded Classes (11th)"

# ✅ असली टाइम टेबल (जो आपने बताया था)
TIMETABLE = """📅 *Class Schedule:*

• *Monday:* - Maths (5:00 PM)
  - Physics (7:00 PM)

• *Tuesday:* - Physics (3:00 PM)
  - Physical Education (9:00 PM)

• *Wednesday:* No Class (Enjoy! 🏖️)

• *Thu - Sat:* - Computer Science (9:00 PM)

• *Sunday:* Test (Time Sir confirm karenge)"""

# ⚠️ यहाँ अपने PDF से "Test Plan" कॉपी-पेस्ट करें
TEST_PLAN = """📝 *Upcoming Test Plan:*
Abhi koi naya test announce nahi hua hai.
(Kripya Group check karein ya Sir se puchein.)"""

# ⚠️ यहाँ फीस और पता (Address) सही कर लें
FEES_INFO = "💰 *Fees Info:* Contact Sir directly for Class 11th/12th Package details."
ADDRESS = "📍 *Location:* Vesu, Surat (Paas wali building ka naam daalein)."
NOTES_LINK = "📚 *Notes Download:* https://drive.google.com/..."

# --- 2. SERVER KEEP-ALIVE (ताकि बोट सोये नहीं) ---
@app.route('/')
def home():
    return "🦁 Bot is Awake via Cron-Job!"

# --- 3. WHATSAPP BRAIN (दिमाग) ---
@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    try:
        # मैसेज को छोटा और साफ करना (Error handling ke saath)
        incoming_msg = request.args.get('msg', '')
        if not incoming_msg:
            return "Empty message"
            
        msg = incoming_msg.lower().strip()
        
        # --- Logic Begins ---
        
        # 1. Greeting (नमस्ते)
        if msg in ['hi', 'hello', 'hey', 'namaste', 'start', 'hii']:
            return (f"👋 Welcome to *{COACHING_NAME}*!\n\n"
                    "Main aapki kya help karu?\n👇 Ye type karein:\n\n"
                    "👉 *Time* (Schedule dekhne ke liye)\n"
                    "👉 *Test* (Test Plan ke liye)\n"
                    "👉 *Notes* (PDFs ke liye)\n"
                    "👉 *Fee* (Fees info)\n"
                    "👉 *Address* (Location)")

        # 2. Time Table (Schedule)
        elif any(word in msg for word in ['time', 'kab', 'schedule', 'class', 'routine']):
            return TIMETABLE

        # 3. Test Plan (Exam)
        elif any(word in msg for word in ['test', 'exam', 'plan', 'syllabus', 'date']):
            return TEST_PLAN

        # 4. Fees
        elif any(word in msg for word in ['fee', 'money', 'paise', 'cost', 'payment']):
            return FEES_INFO

        # 5. Notes/PDF
        elif any(word in msg for word in ['note', 'pdf', 'book', 'material', 'drive']):
            return NOTES_LINK

        # 6. Location
        elif any(word in msg for word in ['address', 'kaha', 'location', 'jagah', 'map', 'shop']):
            return ADDRESS

        # 7. Default Reply (जब कुछ समझ न आए)
        else:
            return (f"🤖 Maaf kijiye, mujhe iska jawab nahi pata.\n\n"
                    "Plz sahi option type karein (Time / Notes / Fee).\n"
                    "Ya direct Sir ko call karein: 📞 9876543210")
          
    except Exception as e:
        # अगर कोई बहुत बड़ी गड़बड़ हो जाए तो यह आएगा
        return "⚠️ Server Error. Please try again."

if __name__ == '__main__':
    # Render ke liye Port fix (Bug Fixed)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
