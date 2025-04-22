from app.logger import get_logger
logger = get_logger(__name__)

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

# Load processor and model (ViT)
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("DEVICE:--------> ",device)
model.to(device)

def generate_caption(image_path: str) -> str:
    logger.info("Generating caption...")
    try:
        # Open and convert image to RGB
        image = Image.open(image_path).convert('RGB')
        
        # Preprocess image and prepare inputs
        inputs = processor(images=image, return_tensors="pt").to(device)

        # Generate caption (greedy decoding for now)
        output = model.generate(**inputs, max_length=16, num_beams=1)
        
        # Decode output to text
        caption = tokenizer.decode(output[0], skip_special_tokens=True)
        
        logger.info(f"Caption generated: {caption}")
        return caption
    except Exception as e:
        logger.exception("Failed to generate caption")
        raise
