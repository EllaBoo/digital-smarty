# 🧠 Digital Smarty v4.0

**Adaptive AI Expert Bot** for audio/video analysis with automatic expertise detection.

## Features

- 🎧 Audio/video transcription (Deepgram Nova-2)
- 🧠 Automatic expertise detection (becomes expert in discussed topic)
- 📊 Professional analysis from expert perspective
- 📄 PDF report generation
- 💬 Q&A with expert context
- 🌍 Multi-language support (RU, EN, KK, ES, ZH)

## Quick Start

1. Clone repository
2. Copy `.env.example` to `.env` and fill credentials
3. Run with Docker: `docker-compose up -d`

## Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

## Environment Variables

- `TELEGRAM_BOT_TOKEN` - Bot token from @BotFather
- `TELEGRAM_API_ID` - From my.telegram.org
- `TELEGRAM_API_HASH` - From my.telegram.org
- `DEEPGRAM_API_KEY` - From deepgram.com
- `OPENAI_API_KEY` - From platform.openai.com

## License

MIT
