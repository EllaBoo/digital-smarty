"""
Translations for Digital Smarty - Full multilingual support
"""

TRANSLATIONS = {
    "ru": {
        "welcome": """👋 Привет! Я **Цифровой Умник** — твой AI-эксперт.

Отправь мне запись (аудио или видео), и я:
• 🎧 Расшифрую речь
• 🧠 Стану экспертом в теме обсуждения
• 🔍 Проведу глубокий профессиональный анализ
• 📄 Создам подробный PDF-отчёт
• 💬 Отвечу на любые вопросы по записи

Я адаптируюсь под тему: маркетинг, продажи, разработка, HR, финансы — что угодно! 🚀""",
        
        "choose_lang": "🌍 На каком языке подготовить анализ?",
        "processing": "⏳ Начинаю обработку...",
        "transcribing": "🎧 Слушаю и расшифровываю речь...",
        "detecting_expertise": "🔍 Определяю тему и становлюсь экспертом...",
        "analyzing_as_expert": "🧠 Анализирую как {expert_role}...",
        "diagnosing": "🔬 Провожу экспертную диагностику...",
        "generating_pdf": "📄 Создаю PDF-отчёт...",
        "done": "✅ Готово!",
        "analysis_complete": """✅ **Анализ завершён!**

📊 Эффективность: {score_emoji} **{score}/100**
📎 Тип: {meeting_type}
🎭 Анализировал как: {expert_role}
⏱️ {duration} • 👥 {speakers} спикер(ов)

{tip}""",
        "ask_question": "❓ Задать вопрос эксперту",
        "get_transcript": "📜 Получить транскрипт",
        "new_analysis": "🔄 Новый анализ",
        "back": "◀️ Назад",
        "question_prompt": "💬 Задай свой вопрос — отвечу как {expert_role}:",
        "thinking": "🤔 Думаю как {expert_role}...",
        "no_data": "❌ Сначала отправь запись для анализа",
        "error": "❌ Произошла ошибка: {error}",
        "file_too_large": "❌ Файл слишком большой. Максимум 100 МБ.",
        "unsupported_format": "❌ Неподдерживаемый формат. Отправь аудио или видео.",
        "expert_tip_intro": "💡 **Совет от {expert_role}:**",
    },
    
    "en": {
        "welcome": """👋 Hi! I'm **Digital Smarty** — your AI expert.

Send me a recording (audio or video), and I will:
• 🎧 Transcribe speech
• 🧠 Become an expert in the topic discussed
• 🔍 Conduct deep professional analysis
• 📄 Create detailed PDF report
• 💬 Answer any questions about the recording

I adapt to any topic: marketing, sales, development, HR, finance — anything! 🚀""",
        
        "choose_lang": "🌍 What language should I use for analysis?",
        "processing": "⏳ Starting processing...",
        "transcribing": "🎧 Listening and transcribing...",
        "detecting_expertise": "🔍 Detecting topic and becoming an expert...",
        "analyzing_as_expert": "🧠 Analyzing as {expert_role}...",
        "diagnosing": "🔬 Conducting expert diagnostics...",
        "generating_pdf": "📄 Generating PDF report...",
        "done": "✅ Done!",
        "analysis_complete": """✅ **Analysis complete!**

📊 Effectiveness: {score_emoji} **{score}/100**
📎 Type: {meeting_type}
🎭 Analyzed as: {expert_role}
⏱️ {duration} • 👥 {speakers} speaker(s)

{tip}""",
        "ask_question": "❓ Ask the expert",
        "get_transcript": "📜 Get transcript",
        "new_analysis": "🔄 New analysis",
        "back": "◀️ Back",
        "question_prompt": "💬 Ask your question — I'll answer as {expert_role}:",
        "thinking": "🤔 Thinking as {expert_role}...",
        "no_data": "❌ Send a recording first",
        "error": "❌ Error occurred: {error}",
        "file_too_large": "❌ File too large. Maximum 100 MB.",
        "unsupported_format": "❌ Unsupported format. Send audio or video.",
        "expert_tip_intro": "💡 **Tip from {expert_role}:**",
    },
}

user_languages = {}

def t(user_id: int, key: str, **kwargs) -> str:
    lang = user_languages.get(user_id, "ru")
    translations = TRANSLATIONS.get(lang, TRANSLATIONS["ru"])
    text = translations.get(key, TRANSLATIONS["ru"].get(key, key))
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    return text

def set_user_lang(user_id: int, lang: str):
    if lang == "auto":
        lang = "ru"
    user_languages[user_id] = lang

def get_user_lang(user_id: int) -> str:
    return user_languages.get(user_id, "ru")

LANG_NAMES = {
    "ru": "русский",
    "en": "English",
    "auto": "русский"
}

def get_lang_name(lang_code: str) -> str:
    return LANG_NAMES.get(lang_code, "русский")
