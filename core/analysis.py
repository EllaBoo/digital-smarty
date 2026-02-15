"""Analysis module - Adaptive Expert System"""
import json
import logging
from openai import AsyncOpenAI
import config

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)

async def detect_expertise(transcript: str, language: str = "ru") -> dict:
    return {
        "domain": "general",
        "domain_localized": "general",
        "meeting_type": "meeting",
        "meeting_type_localized": "meeting",
        "expert_role": "business consultant"
    }

async def analyze_transcript(transcript: str, language: str = "ru", expertise: dict = None) -> str:
    if not expertise:
        expertise = await detect_expertise(transcript, language)
    
    response = await client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": f"You are Digital Smarty, acting as {expertise['expert_role']}. Analyze in {language}."},
            {"role": "user", "content": f"Analyze this transcript:\n\n{transcript[:30000]}"}
        ],
        temperature=0.3,
        max_tokens=4000
    )
    return response.choices[0].message.content

async def answer_question(question: str, transcript: str, analysis: str, language: str = "ru", expertise: dict = None) -> str:
    response = await client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": f"Answer based on transcript. Language: {language}"},
            {"role": "user", "content": f"Transcript: {transcript[:20000]}\n\nQuestion: {question}"}
        ],
        temperature=0.5,
        max_tokens=1500
    )
    return response.choices[0].message.content
