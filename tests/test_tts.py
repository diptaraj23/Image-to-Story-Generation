from app.tts import speak_story

story = """Once upon a time in a quiet village, a curious cat named Whiskers loved to watch the birds from his favorite spot by the window..."""
audio_path = speak_story(story)

print("Audio saved to:", audio_path)
