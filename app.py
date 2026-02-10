import os
from flask import Flask, request

app = Flask(__name__)

# --- CONFIGURATION ---
COACHING_NAME = "Uday Reloaded Classes (11th)"
TIMETABLE = "📅 *Class Schedule:*\nMon: Maths (5 PM)\nTue: Physics (3 PM)\nSun: Test (Confirm with Sir)"

# --- ROOT URL (Jagaane ke liye) ---
@app.route('/')
def home():
    return "🦁 Tuition Bot is Awake!"

# --- WHATSAPP LOGIC ---
@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    incoming_msg = request.args.get('msg', '')
    if not incoming_msg:
        return "🤖 Message khali tha. Text likhkar bhejein."
    
    msg = incoming_msg.lower().strip()
    
    if 'time' in msg or 'kab' in msg:
        return TIMETABLE
    else:
        return f"👋 Welcome to {COACHING_NAME}!\nType: Time, Test, or Notes."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
