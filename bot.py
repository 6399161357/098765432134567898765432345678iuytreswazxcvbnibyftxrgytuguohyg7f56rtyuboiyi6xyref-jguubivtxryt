import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot Token (Replace with your actual token)
BOT_TOKEN = "8838139263:AAGwcOOJ1RSZ9mM6e6tz3XWKc627yM4ha1k"

# Allowed Usernames (without @)
USER1 = "Light_speedy"
USER2 = "Cherry_blossomm"

# Display names with styling
NAME1 = "L ɪ ɢ ʜ ᴛ"
NAME2 = "᥀꯭ᮁ💗׀⃪𝆺꯭𝅥𝐐𝐮𝐞𝐞𝐧⃪💗𝐬𝐚𝐧𝐢𝐲𝐚🌸"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    mention = user.mention_html()
    
    text = (
        f"<b>This bot is made for {NAME2}</b>\n\n"
        f"<i>Powered by</i> <a href='https://t.me/Light_speedy'>L ɪ ɢ ʜ ᴛ</a>\n"
    )
    
    keyboard = [
        [InlineKeyboardButton("L ɪ ɢ ʜ ᴛ", url="https://t.me/Light_speedy")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text, 
        parse_mode="HTML", 
        reply_markup=reply_markup
    )

# /crush command - Only for USER1 and USER2
async def crush(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username
    
    # Check if the user is one of the allowed ones
    if username not in [USER1, USER2]:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return
    
    # Check if replying to a message
    if not update.message.reply_to_message:
        await update.message.reply_text("⚠️ Please reply to the person you want to check crush with.")
        return
    
    replied_user = update.message.reply_to_message.from_user
    replied_username = replied_user.username
    
    # Check if replied user is the other allowed user
    if username == USER1 and replied_username == USER2:
        text = f"<a href='https://t.me/{USER2}'>{NAME2}</a> has 100% crush on <a href='https://t.me/{USER1}'>{NAME1}</a> 💕"
    elif username == USER2 and replied_username == USER1:
        text = f"<a href='https://t.me/{USER1}'>{NAME1}</a> has 100% crush on <a href='https://t.me/{USER2}'>{NAME2}</a> 💕"
    else:
        text = "⚠️ You can only use this command replying to each other (@Light_speedy ↔ @Cherry_blossomm)."
    
    await update.message.reply_text(text, parse_mode="HTML")

# /love command - Only for USER1 and USER2
async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username
    
    if username not in [USER1, USER2]:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return
    
    if not update.message.reply_to_message:
        await update.message.reply_text("⚠️ Please reply to the person you want to check love compatibility with.")
        return
    
    replied_user = update.message.reply_to_message.from_user
    replied_username = replied_user.username
    
    if (username == USER1 and replied_username == USER2) or (username == USER2 and replied_username == USER1):
        text = (
            f"<a href='https://t.me/{USER1}'>{NAME1}</a> ❤️ <a href='https://t.me/{USER2}'>{NAME2}</a>\n\n"
            f"<b>Lᴏᴠᴇ Cᴏᴍᴘᴀᴛɪʙɪʟɪᴛʏ: 100% ❤️</b>"
        )
    else:
        text = "⚠️ This command works only between L ɪ ɢ ʜ ᴛ and ᥀꯭ᮁ💗׀⃪𝆺꯭𝅥𝐐𝐮𝐞𝐞𝐧⃪💗𝐬𝐚𝐧𝐢𝐲𝐚🌸."
    
    await update.message.reply_text(text, parse_mode="HTML")

# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("crush", crush))
    app.add_handler(CommandHandler("love", love))
    
    # Start the bot
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
