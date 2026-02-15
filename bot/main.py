"""
Digital Smarty v4.0 - Main Bot
Adaptive AI expert that becomes professional in recording topic
"""
import asyncio
import logging
import re
from pathlib import Path
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.enums import ParseMode

import config
from bot.translations import t, set_user_lang, get_user_lang, get_lang_name
from bot.keyboards import language_keyboard, main_keyboard, back_keyboard

from core.transcription import transcribe_audio
from core.analysis import analyze_transcript, answer_question, detect_expertise
from core.diagnostics import diagnose_communication
from core.pdf_generator import generate_pdf_report
from core.topic_extractor import extract_main_topic

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Client(
    "digital_smarty_bot",
    api_id=config.TELEGRAM_API_ID,
    api_hash=config.TELEGRAM_API_HASH,
    bot_token=config.TELEGRAM_BOT_TOKEN,
    workdir=str(config.SESSIONS_DIR)
)

user_cache = {}

def get_cache(user_id: int) -> dict:
    if user_id not in user_cache:
        user_cache[user_id] = {}
    return user_cache[user_id]

def format_duration(seconds: float) -> str:
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}:{secs:02d}"

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    uid = message.from_user.id
    await message.reply(t(uid, "welcome"), parse_mode=ParseMode.MARKDOWN)

@app.on_message(filters.audio | filters.video | filters.voice | filters.video_note | filters.document)
async def media_handler(client: Client, message: Message):
    uid = message.from_user.id
    cache = get_cache(uid)
    cache["pending_message"] = message
    await message.reply(t(uid, "choose_lang"), reply_markup=language_keyboard())

if __name__ == "__main__":
    logger.info("🚀 Starting Digital Smarty Bot v4.0...")
    config.SESSIONS_DIR.mkdir(exist_ok=True)
    config.TMP_DIR.mkdir(exist_ok=True)
    app.run()
