from app.logger import get_logger
logger = get_logger(__name__)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model = "google/flan-t5-small"
# Load tokenizer and model
tokenizer =AutoTokenizer.from_pretrained(model)
model = AutoModelForSeq2SeqLM.from_pretrained(model)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_story(caption: str, max_length: int = 256) -> str:
    logger.info("Generating story...")
    try:
        # Turn caption into a story prompt
        prompt = f"""
You are a creative storyteller who writes engaging short stories.

- Length: The story should have around 200-300 words
- Your job is to take the image caption and expand it into a vivid short story.
- Start with an engaging hook, build a little conflict, and wrap up with a satisfying ending.
- Use descriptive language and maintain a consistent tone.

Caption: "{caption}"

Write the story below:
""".strip()

        # Tokenize and run through model
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id,
        early_stopping=True,
        repetition_penalty=1.2,
        length_penalty=1.0)


        # Decode generated text
        story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story.replace(prompt, "").strip()
    except Exception as e:
        logger.exception(f"Failed to generate story: {str(e)}")
        raise
