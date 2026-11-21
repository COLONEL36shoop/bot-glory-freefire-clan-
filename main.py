```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
players = {}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    players[user.id] = players.get(user.id, {"name": user.first_name, "glory": 0})
    await update.message.reply_text(f"اهلا بيك يا بطل {user.first_name} 🔥\nسجلتك في كلان Glory\n\nاكتب /room باش تشوف روم اليوم\nاكتب /top باش تشوف ترتيب الأبطال")
async def room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 روم اليوم تاع Glory 🔥\n\nالروم: 123456\nكلمة السر: glory\nالساعة: 21:00")
async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not players:
        await update.message.reply_text("مازال حتى واحد ما سجل نقاط")
        return
    sorted_players = sorted(players.values(), key=lambda x: x["glory"], reverse=True)
    text = "🏆 ترتيب أبطال Glory 🏆\n\n"
    for i, p in enumerate(sorted_players[:10], 1):
        text += f"{i}. {p['name']} - {p['glory']} نقطة\n"
    await update.message.reply_text(text)
if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("room", room))
    app.add_handler(CommandHandler("top", top))
    print("Bot is running...")
    app.run_polling()
```
