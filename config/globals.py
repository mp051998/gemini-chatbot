
import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")

class SPEAKER_TYPES:
  USER = "user"
  BOT = "bot"
