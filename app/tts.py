from app.logger import get_logger
logger = get_logger(__name__)

from gtts import gTTS
from playsound import playsound
import os
import uuid

def speak_story(story: str, lang: str = 'en') -> str:
    """
    Converts the story text to speech and saves it as an audio file.
    Optionally plays the audio.

    Returns the path to the audio file.
    """
    logger.info("Generating audio...")
    try:
        # Generate a unique filename
        filename = f"story_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join("outputs", filename)

        # Ensure outputs/ directory exists
        os.makedirs("outputs", exist_ok=True)

        # Generate TTS from text
        tts = gTTS(text=story, lang=lang)
        tts.save(filepath)

        # Play the audio (optional)
        try:
            playsound(filepath)
        except Exception as e:
            logger.exception("Couldn't play audio: {e}")

        return filepath
    except Exception as e:
        logger.exception("Failed to generate audio:{e}")
        raise