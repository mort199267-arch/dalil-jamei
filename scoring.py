# أسماء المحاور بالعربي
DIMENSION_NAMES = {
    "LOGIC": "🧠 التفكير المنطقي والرياضي",
    "TECH": "💻 التقنية والأنظمة الرقمية",
    "ENG": "⚙️ الهندسة والتطبيق الميداني",
    "SCI_LIFE": "🩺 العلوم الطبية والحيوية",
    "SCI_PHY": "🔬 العلوم الطبيعية والمخبرية",
    "BUS_FIN": "📊 الإدارة والمال والأعمال",
    "LAW_SOC": "⚖️ القانون والعمل الاجتماعي",
    "LANG_COMM": "🎙️ اللغات والإعلام والاتصال",
    "CREAT_DES": "🎨 الإبداع والتصميم المعماري",
    "RESEARCH": "📚 البحث والاستقصاء الأكاديمي",
    "TEAM_LEAD": "👥 القيادة وإدارة الفرق",
    "DETAIL": "🔎 الدقة والتركيز الإجرائي"
}

# مصفوفة التخصصات وأوزان المحاور
MAJORS_MATRIX = {
    "الطب العام والعلوم الصحية": {
        "weights": {"SCI_LIFE": 0.35, "RESEARCH": 0.20, "DETAIL": 0.20, "SCI_PHY": 0.15, "LAW_SOC": 0.10},
        "reason": "شغف عالي بإنقاذ الأرواح وفهم جسم الإنسان، مع دقة ملاحظة ورغبة مستمرة في البحث."
    },
    "علوم الحاسوب والذكاء الاصطناعي": {
        "weights": {"TECH": 0.40, "LOGIC": 0.30, "RESEARCH": 0.15, "DETAIL": 0.15},
        "reason": "ميل قوي للتفكير المنطقي التجريدي وبناء الخوارزميات والحلول البرمجية الذكية."
    },
    "هندسة الحاسوب والبرمجيات": {
        "weights": {"TECH": 0.35, "ENG": 0.25, "LOGIC": 0.25, "DETAIL": 0.15},
        "reason": "جمع فريد بين عتاد الأجهزة الملموس وتطوير المنظومات الرقمية المتقدمة."
    },
    "الهندسة الكهربائية والإلكترونية": {
        "weights": {"ENG": 0.35, "LOGIC": 0.25, "SCI_PHY": 0.20, "TECH": 0.20},
        "reason": "اهتمام بفهم مسارات الطاقة، الدوائر الكهربائية، والتحكم بالأنظمة الكهرومغناطيسية."
    },
    "الهندسة المدنية والإنشائية": {
        "weights": {"ENG": 0.40, "LOGIC": 0.25, "DETAIL": 0.20, "TEAM_LEAD": 0.15},
        "reason": "شغف بتشييد المشاريع الملموسة والعمل الميداني وإدارة التنفيذ الهندسي."
    },
    "الهندسة المعمارية والتصميم": {
        "weights": {"CREAT_DES": 0.35, "ENG": 0.25, "DETAIL": 0.20, "LOGIC": 0.20},
        "reason": "توازن إبداعي رفيع بين الحس الجمالي والفني وقواعد البناء الإنشائي."
    },
    "الهندسة الميكانيكية": {
        "weights": {"ENG": 0.40, "SCI_PHY": 0.25, "LOGIC": 0.20, "DETAIL": 0.15},
        "reason": "ميل لفهم حركة الآلات والقوى وتصميم المحركات والمنظومات الميكانيكية."
    },
    "هندسة النفط والغاز والطاقة": {
        "weights": {"ENG": 0.35, "SCI_PHY": 0.25, "LOGIC": 0.20, "TEAM_LEAD": 0.20},
        "reason": "جاهزية للعمل في المواقع الحيوية الكبرى والتعامل مع تكنولوجيا استخراج وتكرير الطاقة."
    },
    "إدارة الأعمال والتسويق الدولي": {
        "weights": {"BUS_FIN": 0.35, "TEAM_LEAD": 0.30, "LANG_COMM": 0.20, "LOGIC": 0.15},
        "reason": "شخصية قيادية تتميز بمهارات التفاوض، التخطيط الاستراتيجي واستثمار الفرص."
    },
    "المحاسبة والعلوم المالية والمصرفية": {
        "weights": {"BUS_FIN": 0.40, "DETAIL": 0.30, "LOGIC": 0.20, "TECH": 0.10},
        "reason": "دقة استثنائية في قراءة الأرقام والبيانات، وتتبع مسارات التدفقات النقدية."
    },
    "القانون والعلوم الجنائية": {
        "weights": {"LAW_SOC": 0.40, "LANG_COMM": 0.25, "LOGIC": 0.20, "RESEARCH": 0.15},
        "reason": "قوة الحجة والبيان، وحب الدفاع عن الحقوق والتحليل المنطقي للنصوص التشريعية."
    },
    "الإعلام والاتصال وصناعة المحتوى": {
        "weights": {"LANG_COMM": 0.40, "CREAT_DES": 0.25, "LAW_SOC": 0.20, "TEAM_LEAD": 0.15},
        "reason": "قدرة تأثيرية عالية في الخطاب ونقل الحقائق واستخدام الوسائط الرقمية باحتراف."
    },
    "اللغات والترجمة والأدب": {
        "weights": {"LANG_COMM": 0.45, "RESEARCH": 0.25, "LAW_SOC": 0.15, "DETAIL": 0.15},
        "reason": "تذوق لغوي عميق، وفضول ثقافي للربط بين الشعوب من خلال صياغة وترجمة النصوص."
    },
    "العلوم الصرفة (فيزياء / كيمياء)": {
        "weights": {"SCI_PHY": 0.40, "RESEARCH": 0.25, "LOGIC": 0.20, "DETAIL": 0.15},
        "reason": "تساؤل مستمر حول ظواهر الكون، شغف بالتجارب المعملية وسبر أغوار المادة والطاقة."
    },
    "التعليم الأكاديمي والتدريس": {
        "weights": {"RESEARCH": 0.30, "LANG_COMM": 0.25, "TEAM_LEAD": 0.25, "LAW_SOC": 0.20},
        "reason": "رغبة صادقة في نقل المعرفة، تبسيط العلوم، وغرس الأثر في بناء وتأهيل الأجيال."
    }
}

def calculate_scores(user_answers, questions):
    # حساب المجموع الفعلي
    actual_scores = {k: 0 for k in DIMENSION_NAMES.keys()}
    max_scores = {k: 0 for k in DIMENSION_NAMES.keys()}
    
    # حساب الحد الأقصى الممكن لكل محور من جميع الأسئلة
    for q in questions:
        q_max = {k: 0 for k in DIMENSION_NAMES.keys()}
        for opt in q["options"]:
            for dim, pts in opt["points"].items():
                if pts > q_max[dim]:
                    q_max[dim] = pts
        for dim, pts in q_max.items():
            max_scores[dim] += pts

    # حساب ما اختاره الطالب
    for q_idx, opt_idx in user_answers.items():
        q_idx = int(q_idx)
        if q_idx < len(questions):
            opt = questions[q_idx]["options"][opt_idx]
            for dim, pts in opt["points"].items():
                actual_scores[dim] += pts

    # تحويل إلى نسب مئوية
    percentages = {}
    for dim, total in actual_scores.items():
        max_possible = max_scores.get(dim, 1)
        pct = round((total / max_possible) * 100) if max_possible > 0 else 0
        percentages[dim] = min(pct, 100)

    # حساب التوافق مع التخصصات
    majors_results = []
    for major_name, data in MAJORS_MATRIX.items():
        w_sum = sum(data["weights"].values())
        weighted_score = sum(percentages.get(dim, 0) * weight for dim, weight in data["weights"].items())
        final_major_pct = round(weighted_score / w_sum) if w_sum > 0 else 0
        majors_results.append({
            "name": major_name,
            "percentage": final_major_pct,
            "reason": data["reason"]
        })

    # ترتيب التخصصات تنازلياً من الأعلى توافقاً للأقل
    majors_results.sort(key=lambda x: x["percentage"], reverse=True)

    return percentages, majors_results
