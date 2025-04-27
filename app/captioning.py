from app.logger import get_logger
logger = get_logger(__name__)

import torch
from PIL import Image
from transformers import ViTFeatureExtractor, AutoTokenizer, VisionEncoderDecoderModel

model_id = "ydshieh/vit-gpt2-coco-en"

# Load model, tokenizer, and image processor
feature_extractor = ViTFeatureExtractor.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = VisionEncoderDecoderModel.from_pretrained(model_id)
model.eval()

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logger.info(f"DEVICE:--------> {device}")
model.to(device)

def generate_caption(image_path: str) -> str:
    logger.info("Generating caption...")
    try:
        # Open and convert image to RGB
        image = Image.open(image_path).convert('RGB')
        
        # Preprocess image and prepare inputs
        pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.to(device)

        # Generate caption (greedy decoding for now)
        with torch.no_grad():
            output_ids = model.generate(pixel_values, max_length=16, num_beams=4, return_dict_in_generate=True).sequences

        preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        caption = [pred.strip() for pred in preds]

        return caption
    except Exception as e:
        logger.exception("Failed to generate caption")
        raise
