"""Keyboards for Digital Smarty bot"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.translations import t

def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Auto-detect", callback_data="lang_auto")],
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ],
    ])

def main_keyboard(user_id: int, expert_role: str = "") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(user_id, "ask_question"), callback_data="ask")],
        [InlineKeyboardButton(t(user_id, "get_transcript"), callback_data="transcript")],
        [InlineKeyboardButton(t(user_id, "new_analysis"), callback_data="new")],
    ])

def back_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(user_id, "back"), callback_data="back")]
    ])
