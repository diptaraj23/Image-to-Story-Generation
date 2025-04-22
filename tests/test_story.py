# test_story.py

from app.storytelling import generate_story

caption = "a group of people standing in a pool"
story = generate_story(caption)
print("Generated Story:\n", story)
