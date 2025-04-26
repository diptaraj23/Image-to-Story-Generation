from app.logger import get_logger
logger = get_logger(__name__)

from transformers import AutoTokenizer, AutoImageProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

model_id = "cnmoro/nano-image-captioning"
# Load model, tokenizer, and image processor
model = VisionEncoderDecoderModel.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
image_processor = AutoImageProcessor.from_pretrained(model_id)

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
        inputs = image_processor(images=image, return_tensors="pt").to(device)

        # Generate caption (greedy decoding for now)
        output = model.generate(**inputs, max_length=30, num_beams=1)
        
        # Decode output to text
        caption = tokenizer.decode(output[0], skip_special_tokens=True)
        
        logger.info(f"Caption generated: {caption}")
        return caption
    except Exception as e:
        logger.exception("Failed to generate caption")
        raise
