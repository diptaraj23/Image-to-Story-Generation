import os
import argparse
from app.captioning import generate_caption
from app.storytelling import generate_story
from app.tts import speak_story

def main(file_name):
    image_path = os.path.join(os.path.dirname(__file__), "assets",file_name)
    print("🔍 Generating caption from image...")
    caption = generate_caption(image_path)
    print(f"\n🖼️  Caption: {caption}")

    print("\n✍️  Generating story from caption...")
    story = generate_story(caption)
    print(f"\n📖 Story:\n{story}")

    print("\n🔊 Converting story to speech...")
    audio_path = speak_story(story)
    print(f"\n✅ Audio saved at: {audio_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run image → caption → story → speech pipeline")
    parser.add_argument("image_path", type=str, help="Path to the input image")

    args = parser.parse_args()
    main(args.image_path)
