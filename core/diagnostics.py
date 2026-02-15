"""Diagnostics module"""
import logging
from openai import AsyncOpenAI
import config

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)

async def diagnose_communication(transcript: str, language: str = "ru", expertise: dict = None) -> str:
    response = await client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": f"Diagnose communication quality. Language: {language}"},
            {"role": "user", "content": f"Transcript: {transcript[:30000]}"}
        ],
        temperature=0.3,
        max_tokens=3000
    )
    return response.choices[0].message.content
