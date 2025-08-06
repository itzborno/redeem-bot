from keep_alive import keep_alive
import telebot

# বট টোকেন দিন (নিরাপত্তার জন্য GitHub এ .env ব্যবহার করা ভালো)
TOKEN = '7798531358:AAGq2Wo2lFJ3zVz4rX2oxjOL-iWMHELH-Mo'
bot = telebot.TeleBot(TOKEN)

# Keep alive HTTP server চালু করা (Render এ port bind করার জন্য)
keep_alive()

# ১০টি ইউনিক রিডিম কোড + মেসেজ
valid_codes = {
    'CODE1': 'ottraya@yahoo.com:MPXbghm5 | Email verified = true | Plan = 〖〗-[cr_premium.1_month] | Subscription = true | Expiry = 2025-08-17 | Remaining days = 10 | Country = United States 🇺🇸 | Config by = 🔥 @Itzborno67 🔥',
    'CODE2': 'pvlc1999@gmail.com:Feliciana99 | Email verified = true | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-28 | Remaining days = 21 | Country = Peru 🇵🇪 | Config by = 🔥 @Itzborno67 🔥',
    'CODE3': 'rz72458@gmail.com:Rz00172458$$$ | Email verified = true | Plan = 〖FAN MEMBER〗-[cr_premium.3_month] | Subscription = true | Expiry = 2025-08-14 | Remaining days = 7 | Country = United States 🇺🇸 | Config by = 🔥 @Itzborno67 🔥',
    'CODE4': 'joacoyt466@gmail.com:joaquinocampo10() | Email verified = true | Plan = 〖〗-[cr_fan_pack.1_year] | Subscription = true | Expiry = 2026-06-15 | Remaining days = 312 | Country = Argentina 🇦🇷 | Config by = 🔥 @Itzborno67 🔥',
    'CODE5': 'jamibanez.es@gmail.com:Kyuubi0992 | Email verified = true | Plan = 〖MEGA FAN MEMBER〗-[cr.ios.fanpack.annually] | Subscription = false | Expiry = 2026-02-14 | Remaining days = 191 | Country = El Salvador 🇸🇻 | Config by = 🔥 @Itzborno67 🔥',
    'CODE6': 'christianebeatricetimmermann@outlook.de:Crnchyrll25% | Email verified = true | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-25 | Remaining days = 18 | Country = Germany 🇩🇪 | Config by = 🔥 @Itzborno67 🔥',
    'CODE7': 'lillypops29@icloud.com:Lewbylew29 | Email verified = false | Plan = 〖〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-14 | Remaining days = 7 | Country = United Kingdom 🇬🇧 | Config by = 🔥 @Itzborno67 🔥',
    'CODE8': 'juancarloszabalaaldana@gmail.com:(Lunajk2184) | Email verified = true | Plan = 〖〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-12 | Remaining days = 5 | Country = United States 🇺🇸 | Config by = 🔥 @Itzborno67 🔥',
    'CODE9': 'Muk8227@gmail.com:+z4ZF6EQLrJ#_jk | Email verified = false | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-18 | Remaining days = 11 | Country = United States 🇺🇸 | Config by = 🔥 @Itzborno67 🔥',
    'CODE10': 'Nicolas.Kirschwing@hotmail.fr:Crunchyray1965! | Email verified = true | Plan = 〖MEGA FAN MEMBER〗-[cr_fan_pack.1_month] | Subscription = true | Expiry = 2025-08-25 | Remaining days = 20 | Country = France 🇫🇷 | Config by = 🔥 @Itzborno67 🔥',
}

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

