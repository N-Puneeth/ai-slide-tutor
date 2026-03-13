import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME", "llama3-70b-8192")

TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))

MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1200))

APP_NAME = "AI Slide Tutor Backend"

API_VERSION = "1.0"