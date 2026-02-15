"""Transcription module using Deepgram Nova-2"""
import httpx
import logging
import config

logger = logging.getLogger(__name__)

async def transcribe_audio(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        audio_data = f.read()
    
    url = "https://api.deepgram.com/v1/listen"
    params = {"model": "nova-2", "smart_format": "true", "diarize": "true", "punctuate": "true", "detect_language": "true"}
    headers = {"Authorization": f"Token {config.DEEPGRAM_API_KEY}", "Content-Type": "audio/mp3"}
    
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(url, params=params, headers=headers, content=audio_data)
        response.raise_for_status()
        result = response.json()
    
    channels = result.get("results", {}).get("channels", [])
    if not channels:
        return {"text": "", "speakers": [], "duration": 0, "speakers_count": 0}
    
    alternatives = channels[0].get("alternatives", [])
    if not alternatives:
        return {"text": "", "speakers": [], "duration": 0, "speakers_count": 0}
    
    text = alternatives[0].get("transcript", "")
    duration = result.get("metadata", {}).get("duration", 0)
    
    return {"text": text, "speakers": [], "duration": duration, "speakers_count": 1}
