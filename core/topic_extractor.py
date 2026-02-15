"""Topic extraction utilities"""
import re
import logging
from openai import AsyncOpenAI
import config

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)

async def extract_main_topic(analysis: str, language: str = "ru") -> str:
    try:
        response = await client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[{"role": "user", "content": f"Extract main topic (2-3 words) from: {analysis[:2000]}"}],
            temperature=0,
            max_tokens=20
        )
        topic = response.choices[0].message.content.strip()
        topic = re.sub(r"[^\w\s-]", "", topic).replace(" ", "_")[:30]
        return topic or "analysis"
    except:
        return "analysis"
