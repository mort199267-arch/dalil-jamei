from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from questions import QUESTIONS
from scoring import calculate_scores, DIMENSION_NAMES
from database import save_user_result, get_user_result

TOTAL_QUESTIONS = len(QUESTIONS)

def get_progress_bar(current, total=50, bar_length=15):
    filled = int(round(bar_length * current / float(total)))
    bar = '█' * filled + '░' * (bar_length - filled)
    return bar

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        "🎓 *أهلاً بك في بوت دليل جامعي*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "دليلك الأكاديمي الذكي لاكتشاف ميولك وتحديد التخصصات والمجالات الجامعية "
        "التي تتوافق تماماً مع طريقة تفكيرك، اهتماماتك ونمط شخصيتك.\n\n"
        "🧠 يتكون الاختبار من 50 سؤالاً وموقفاً مدروساً بعناية.\n"
        "⏱️ لا تتسرع، واختر ما يعبر عنك بصدق وواقعية.\n"
    )
    
    keyboard = [
        [InlineKeyboardButton("🧠 ابدأ الاختبار الآن", callback_data="start_quiz")],
        [InlineKeyboardButton("📊 نتيجتي السابقة", callback_data="my_result")],
        [InlineKeyboardButton("ℹ️ عن دليل جامعي", callback_data="about_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.edit_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, q_index: int):
    query = update.callback_query
    q_data = QUESTIONS[q_index]
    progress_bar = get_progress_bar(q_index + 1, TOTAL_QUESTIONS)
    
    text = (
        f"📝 *السؤال {q_index + 1} من {TOTAL_QUESTIONS}*\n"
        f"`{progress_bar}`\n\n"
        f"*{q_data['text']}*\n"
    )
    
    keyboard = []
    # توليد الأزرار للخيارات الستة
    for opt_idx, opt in enumerate(q_data["options"]):
        keyboard.append([InlineKeyboardButton(opt["text"], callback_data=f"ans_{q_index}_{opt_idx}")])
        
    # زر الرجوع للسؤال السابق إذا لم يكن الأول
    nav_buttons = []
    if q_index > 0:
        nav_buttons.append(InlineKeyboardButton("◀️ السؤال السابق", callback_data=f"prev_{q_index}"))
    nav_buttons.append(InlineKeyboardButton("❌ إلغاء الاختبار", callback_data="cancel_quiz"))
    keyboard.append(nav_buttons)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if query:
        await query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.effective_message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    user = update.effective_user
    await query.answer()
    
    # تهيئة بيانات المستخدم في context إذا لم تكن موجودة
    if "answers" not in context.user_data:
        context.user_data["answers"] = {}
        
    if data == "start_quiz" or data == "restart_quiz":
        context.user_data["answers"] = {}
        await send_question(update, context, 0)
        return
        
    if data == "cancel_quiz":
        context.user_data["answers"] = {}
        await query.message.edit_text("تم إلغاء الاختبار بنجاح. يمكنك العودة والبدء في أي وقت عبر أمر /start.")
        return
        
    if data == "about_bot":
        about_text = (
            "🎓 *حول مشروع دليل جامعي*\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "أداة استرشادية ذكية مخصصة لمساعدة طلبة العراق في مرحلة ما بعد الإعدادية "
            "على اكتشاف شغفهم العلمي وميولهم عبر مقياس متعدد الأبعاد يحلل التفكير المنطقي، "
            "الهندسي، الطبي، الاجتماعي، والإبداعي.\n\n"
            "⚠️ الاختبار لا يقرر مستقبلك بدلاً منك، بل يعطيك رؤية موضوعية مبنية على إجاباتك."
        )
        keyboard = [[InlineKeyboardButton("🔙 العودة للرئيسية", callback_data="back_home")]]
        await query.message.edit_text(about_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        return

    if data == "back_home":
        await start_command(update, context)
        return

    if data == "my_result":
        saved = get_user_result(user.id)
        if not saved:
            await query.message.edit_text(
                "لم تسجل أي نتيجة سابقة حتى الآن. ابدأ الاختبار لاكتشاف تخصصاتك!",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 ابدأ الاختبار الآن", callback_data="start_quiz")]])
            )
            return
        await display_final_result(query, saved["scores"], saved["top_majors"], from_db=True, completed_at=saved["completed_at"])
        return

    if data.startswith("prev_"):
        curr_q = int(data.split("_")[1])
        prev_q = curr_q - 1
        await send_question(update, context, prev_q)
        return

    if data.startswith("ans_"):
        parts = data.split("_")
        q_idx = int(parts[1])
        opt_idx = int(parts[2])
        
        # حفظ الإجابة
        context.user_data["answers"][q_idx] = opt_idx
        
        # هل اكتملت الأسئلة؟
        if q_idx + 1 < TOTAL_QUESTIONS:
            await send_question(update, context, q_idx + 1)
        else:
            # انتهاء الاختبار واحتساب النتائج
            scores, top_majors = calculate_scores(context.user_data["answers"], QUESTIONS)
            
            # حفظ النتيجة في SQLite
            save_user_result(
                user_id=user.id,
                full_name=user.full_name,
                username=user.username,
                answers=context.user_data["answers"],
                scores=scores,
                top_majors=top_majors
            )
            
            await display_final_result(query, scores, top_majors)
        return

    if data == "show_details":
        saved = get_user_result(user.id)
        if saved:
            scores = saved["scores"]
            lines = ["📊 *التحليل التفصيلي لدرجات المحاور الـ 12:*", "━━━━━━━━━━━━━━━━━━━━"]
            # ترتيب المحاور تنازلياً
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for dim, pct in sorted_scores:
                bar = get_progress_bar(pct, 100, 10)
                name = DIMENSION_NAMES.get(dim, dim)
                lines.append(f"{name}: *{pct}%*\n`{bar}`")
                
            keyboard = [
                [InlineKeyboardButton("🎓 التخصصات المقترحة", callback_data="my_result")],
                [InlineKeyboardButton("🔄 إعادة الاختبار", callback_data="restart_quiz")]
            ]
            await query.message.edit_text("\n".join(lines), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        return

async def display_final_result(query, scores, top_majors, from_db=False, completed_at=None):
    # أعلى 5 تخصصات متوافقة
    best_5 = top_majors[:5]
    
    majors_text = ""
    for idx, m in enumerate(best_5, 1):
        majors_text += f"{idx}. *{m['name']}* — `{m['percentage']}%`\n   _{m['reason']}_\n\n"
        
    # استخراج أبرز 3 نقاط قوة
    sorted_dims = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    strengths_text = "\n".join([f"• {DIMENSION_NAMES.get(dim, dim)} (`{pct}%`)" for dim, pct in sorted_dims])
    
    date_info = f"\n📅 تاريخ إنجاز الاختبار: {completed_at}\n" if from_db and completed_at else ""
    
    result_msg = (
        "🎓 *نتيجة اختبارك — دليل جامعي*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"{date_info}"
        "المجالات والتخصصات الأكثر توافقاً مع نمط إجاباتك:\n\n"
        f"{majors_text}"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌟 *نقاط قوتك الشخصية الأبرز:*\n"
        f"{strengths_text}\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚠️ *ملاحظة هامة:*\n"
        "هذه النتيجة مبنية على خياراتك وأنماط إجاباتك في الاختبار، وهي أداة استرشادية "
        "لمساعدتك على استكشاف شغفك وليست حكماً نهائياً على مستقبلك الجامعي."
    )
    
    keyboard = [
        [InlineKeyboardButton("📊 تحليل مفصل للمحاور", callback_data="show_details")],
        [InlineKeyboardButton("🔄 إعادة الاختبار", callback_data="restart_quiz")],
        [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_home")]
    ]
    
    await query.message.edit_text(result_msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
