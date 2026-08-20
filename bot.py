from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8625259218:AAFBcN2jn1W6NPNH7b64I72U7L-QcQD-Aps"

LESSON1_FILE_ID = "BQACAgQAAxkBAAMjaodLCZDbNq_VcEALHqnFy4vtom4AAhAfAAKb6kBQ6EFBvSTdwl49BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("المستوى 1", callback_data="level_1"), InlineKeyboardButton("المستوى 2", callback_data="level_2")],
        [InlineKeyboardButton("المستوى 3", callback_data="level_3"), InlineKeyboardButton("المستوى 4", callback_data="level_4")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text("مرحباً بك! اختر المستوى الدراسي:", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text("اختر المستوى الدراسي:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("level_"):
        level = data.split("_")[1]
        keyboard = [
            [InlineKeyboardButton("الترم الأول", callback_data=f"term_1_{level}"), InlineKeyboardButton("الترم الثاني", callback_data=f"term_2_{level}")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main_menu")]
        ]
        await query.edit_message_text(f"المستوى {level} - اختر الترم:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("term_"):
        _, term, level = data.split("_")
        if level == "1" and term == "1":
            keyboard = [
                [InlineKeyboardButton("📖 ثقافة إسلامية", callback_data="sub_l1_t1_1")],
                [InlineKeyboardButton("📐 رياضيات", callback_data="sub_l1_t1_2")],
                [InlineKeyboardButton("💻 مهارات حاسوب", callback_data="sub_l1_t1_3")],
                [InlineKeyboardButton("🖥️ أساسيات تقنية معلومات", callback_data="sub_l1_t1_4")],
                [InlineKeyboardButton("🇬🇧 English", callback_data="sub_l1_t1_5")],
                [InlineKeyboardButton("📊 محاسبة مالية", callback_data="sub_l1_t1_6")],
                [InlineKeyboardButton("⬅️ رجوع", callback_data="level_1")]
            ]
        elif level == "2" and term == "1":
            keyboard = [
                [InlineKeyboardButton("💻 VB.NET", callback_data="sub_l2_t1_1")],
                [InlineKeyboardButton("🧩 OOP", callback_data="sub_l2_t1_2")],
                [InlineKeyboardButton("🗄️ DBMS", callback_data="sub_l2_t1_3")],
                [InlineKeyboardButton("🇬🇧 انجليزي تقني", callback_data="sub_l2_t1_4")],
                [InlineKeyboardButton("🌐 PHP", callback_data="sub_l2_t1_5")],
                [InlineKeyboardButton("📊 تحليل وتصميم نظم", callback_data="sub_l2_t1_6")],
                [InlineKeyboardButton("🔌 شبكات 1", callback_data="sub_l2_t1_7")],
                [InlineKeyboardButton("⬅️ رجوع", callback_data="level_2")]
            ]
        elif level == "3" and term == "1":
            keyboard = [
                [InlineKeyboardButton("🗄️ إدارة قواعد بيانات", callback_data="sub_l3_t1_1")],
                [InlineKeyboardButton("🌐 ASP.NET", callback_data="sub_l3_t1_2")],
                [InlineKeyboardButton("📱 أندرويد", callback_data="sub_l3_t1_3")],
                [InlineKeyboardButton("🐧 لينكس", callback_data="sub_l3_t1_4")],
                [InlineKeyboardButton("⚙️ هندسة برمجيات", callback_data="sub_l3_t1_5")],
                [InlineKeyboardButton("📡 اتصال بيانات", callback_data="sub_l3_t1_6")],
                [InlineKeyboardButton("🗣️ مهارات اتصال", callback_data="sub_l3_t1_7")],
                [InlineKeyboardButton("⬅️ رجوع", callback_data="level_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("قريباً إدراج المواد...", callback_data="none")],
                [InlineKeyboardButton("⬅️ رجوع", callback_data=f"level_{level}")]
            ]
        await query.edit_message_text(f"المستوى {level} - اختر المادة:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("sub_"):
        if data == "sub_l1_t1_4":
            keyboard = [
                [InlineKeyboardButton("📄 الدرس الأول (PDF)", callback_data="send_pdf_lesson1")],
                [InlineKeyboardButton("⬅️ رجوع للمواد", callback_data="term_1_1")]
            ]
            await query.edit_message_text("🖥️ **مادة أساسيات تقنية المعلومات**\n\nاختر الدرس لتحميل الملزمة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        else:
            keyboard = [[InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]]
            await query.edit_message_text("📚 الملزمة غير متوفرة حالياً لهذه المادة.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "send_pdf_lesson1":
        await query.message.reply_document(document=LESSON1_FILE_ID, caption="🎓 **كلية سنحان المجتمع**\n\n🛠 **المهندس خالد الطالب**")
    elif data == "main_menu":
        await start(update, context)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("جاري تشغيل البوت...")
    app.run_polling()

if __name__ == "__main__":
    main()
