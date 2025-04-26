from app.logger import get_logger
logger = get_logger(__name__)

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer =AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_story(caption: str, max_length: int = 256) -> str:
    logger.info("Generating story...")
    try:
        # Turn caption into a story prompt
        prompt = (
        "<|system|>\n"
        "You are a helpful assistant.</s>\n"
        "<|user|>\n"
        f"Write a complete, short story about {caption}. Make sure the story has a clear ending.\n</s>\n"
        "<|assistant|>\n"
        )

        # Tokenize and run through model
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=1000,
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            top_k=50,
            eos_token_id=tokenizer.eos_token_id
            )


        # Decode and clean output
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        generated_story = generated_text[len(prompt):]  # Strip prompt part
        
        return generated_story.replace(prompt, "").strip()
    except Exception as e:
        logger.exception(f"Failed to generate story: {str(e)}")
        raise
