from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # User ka message aayega (lowercase mein convert karke)
    incoming_msg = request.values.get('Body', '').lower().strip()
    
    # Twilio ka response object create karein
    resp = MessagingResponse()
    msg = resp.message()

    # --- CONTENT VARIABLES (Yahan apne Links update karein) ---
    VISITING_CARD_LINK = "https://example.com/visiting-card"  # Apna asli link yahan dalein
    RATE_PDF_LINK = "https://drive.google.com/file/d/your-pdf-link" # Apni PDF ka link
    CATALOG_LINK = "https://wa.me/c/917046769047" # WhatsApp Catalog link
    
    # --- LOGIC ---

    # 1. MAIN MENU (Agar koi 'hi', 'hello', 'menu' likhe)
    if incoming_msg in ['hi', 'hello', 'menu', 'start', 'namaste']:
        response_text = (
            "✨🙏 *Namaste! Welcome to Pandey Colour* 🎨\n"
            "t_\"Ghar Aisa, Jo Sabka Mann Moh Le\"_\n\n"
            "👤 **Prop:** Markandey Pandey\n"
            f"🪪 **Digital Visiting Card:** {VISITING_CARD_LINK}\n\n"
            "👇 **Neeche diye gaye number reply karein:**\n\n"
            "1️⃣ 💰 **Rates & Estimate** (Kharcha)\n"
            "2️⃣ 📞 **Contact & Address** (Sampark)\n"
            "3️⃣ 🎨 **Fantak / Shade Card** (Colour Pasand)\n"
            "4️⃣ 🖼️ **Latest Designs** (Album)\n"
            "5️⃣ 💸 **Payment Details**\n\n"
            "_Reply with 1, 2, 3, 4, or 5_"
        )
        msg.body(response_text)

    # 2. OPTION 1: RATES
    elif incoming_msg == '1':
        response_text = (
            "📊 **Pandey Colour - Rate List**\n\n"
            "🔹 **Plastic Paint:** ₹12 - ₹18 / sq.ft\n"
            "🔹 **Royal Play Texture:** ₹25 - ₹40 / sq.ft\n"
            "🔹 **PU Polish:** ₹XXX / sq.ft\n"
            "🔹 **Waterproofing:** Site visit ke baad\n\n"
            f"📄 **Download Full Rate List:** {RATE_PDF_LINK}\n\n"
            "📞 **Call for Estimate:** 70467 69047"
        )
        msg.body(response_text)

    # 3. OPTION 2: CONTACT
    elif incoming_msg == '2':
        response_text = (
            "📞 **Humse Sampark Karein**\n\n"
            "👨‍💼 **Markandey Pandey** (Senior Contractor)\n"
            "📱 +91 70467 69047\n"
            "📱 +91 90167 21639\n\n"
            "📍 **Address:**\n"
            "211/-2 Krishnakunj Society,\n"
            "Palanpur Jakatnaka, Surat.\n\n"
            "🕐 **Time:** 9:00 AM - 8:00 PM"
        )
        msg.body(response_text)
        # Location (Optional - alag message mein bhej sakte hain)
        # msg.media("https://maps.google.com/...") 

    # 4. OPTION 3: FANTAK (COLORS)
    elif incoming_msg == '3':
        response_text = (
            "🎨 **Apne Sapno Ka Colour Chunein**\n\n"
            "Asian Paints ya Nerolac ke shades dekhne ke liye link open karein:\n\n"
            "🌈 **Digital Shade Card:**\n"
            "https://www.asianpaints.com/catalogue/colour-catalogue.html\n\n"
            "💡 *Tip:* Pasand karke screenshot bhejein!"
        )
        msg.body(response_text)

    # 5. OPTION 4: DESIGNS
    elif incoming_msg == '4':
        response_text = (
            "🖼️ **Hamare Latest Designs** ✨\n\n"
            "Humne Royal Play, Texture aur PU Polish ke kayi premium projects kiye hain.\n\n"
            f"📸 **Photos Dekhein:** {CATALOG_LINK}\n\n"
            "🎥 Video call ke liye abhi call karein!"
        )
        msg.body(response_text)

    # 6. OPTION 5: PAYMENT
    elif incoming_msg == '5':
        response_text = (
            "💸 **Payment Details**\n\n"
            "🏦 **UPI ID:** `7046769047@ybl`\n"
            "📱 **GPay / PhonePe:** 70467 69047\n\n"
            "⚠️ *Payment ka screenshot zaroor bhejein.*"
        )
        msg.body(response_text)

    # DEFAULT MESSAGE (Agar kuch aur type kare)
    else:
        msg.body("❌ Galat option. Main Menu ke liye *'Hi'* likh kar bhejein.")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
