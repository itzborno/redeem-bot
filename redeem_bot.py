import telebot

# BotFather থেকে পাওয়া টোকেন এখানে বসান
TOKEN = '7798531358:AAGq2Wo2lFJ3zVz4rX2oxjOL-iWMHELH-Mo'
bot = telebot.TeleBot(TOKEN)

# ১০টি ইউনিক রিডিম কোড + রিডিম হলে কি মেসেজ দিবেন (আপনার মতো করে দিতে পারেন)
valid_codes = {
    'CODE1': 'THE CODE ALREADY IS REDEEMED',
    'CODE2': 'THE CODE ALREADY IS REDEEMED',
    'CODE3': 'keanuosten1@gmail.com:Keanu789! | Email verified = false | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-25 | Remaining days = 20 | Country = United States 🇺🇸 | Config by = 🔥 @Itzborno67 🔥',
    'CODE4': 'THE CODE ALREADY IS REDEEMED',
    'CODE5': 'Nicolas.Kirschwing@hotmail.fr:Crunchyray1965! | Email verified = true | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-25 | Remaining days = 20 | Country = France 🇫🇷 | Config by = 🔥 @Itzborno67 🔥',
    'CODE6': 'THE CODE ALREADY IS REDEEMED',
    'CODE7': 'THE CODE ALREADY IS REDEEMED',
    'CODE8': 'THE CODE ALREADY IS REDEEMED',
    'CODE9': 'THE CODE ALREADY IS REDEEMED',
    'CODE10': 'THE CODE ALREADY IS REDEEMED',
}

# ইউজড কোড গুলো সেভ রাখার জন্য সেট (মেমোরি তে)
used_codes = set()

@bot.message_handler(commands=['redeem'])
def handle_redeem(message):
    parts = message.text.split()

    if len(parts) != 2:
        bot.reply_to(message, "⚠️ সঠিক ফরম্যাট ব্যবহার করুন: /redeem আপনার_কোড")
        return

    code = parts[1].strip().upper()

    if code in used_codes:
        bot.reply_to(message, "❌ এই কোডটি আগেই ব্যবহৃত হয়েছে।")
    elif code in valid_codes:
        used_codes.add(code)
        bot.reply_to(message, f"✅ সফলভাবে রিডিম হয়েছে! {valid_codes[code]}")
    else:
        bot.reply_to(message, "❌ ভুল কোড বা অবৈধ কোড।")

# বট চালু করা
bot.polling()


