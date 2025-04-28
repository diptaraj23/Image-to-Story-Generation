---
title: Your Space Title
emoji: 🚀
colorFrom: indigo
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
---

# GenAI Storyteller
GenAI Storyteller is a Streamlit-based application that transforms images into captivating stories and narrates them aloud. The application leverages state-of-the-art AI models for image captioning, story generation, and text-to-speech conversion.

## Features

- **Image Captioning**: Automatically generates captions for uploaded images using a Vision-Encoder-Decoder model.
- **Story Generation**: Creates a short, coherent story based on the generated caption using a language model.
- **Text-to-Speech**: Converts the generated story into audio using Google Text-to-Speech (gTTS).
- **Streamlit Interface**: Provides an intuitive web interface for users to upload images and interact with the pipeline.

## How It Works

1. **Upload an Image**: Users upload an image via the Streamlit interface.
2. **Generate Caption**: The app generates a caption for the image using a pre-trained Vision-Encoder-Decoder model.
3. **Generate Story**: A short story is created based on the caption using a language model.
4. **Text-to-Speech**: The story is converted into an audio file, which can be played directly in the app.

## Installation

### Prerequisites

- Python 3.11 or higher
- [Hugging Face account](https://huggingface.co/) with an API token
- [Streamlit](https://streamlit.io/) installed

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/diptaraj23/Image-to-Story-Generation.git
   cd genai-storyteller
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Hugging Face API token to `.streamlit/secrets.toml`:
   ```toml
   [HF_TOKEN]
   HF_TOKEN = "your_hugging_face_api_token"
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

6. Open the app in your browser at `http://localhost:8501`.

## File Structure

```
genai-storyteller/
├── app/
│   ├── __init__.py
│   ├── captioning.py         # Image captioning logic
│   ├── storytelling.py       # Story generation logic
│   ├── tts.py                # Text-to-speech conversion
│   ├── logger.py             # Logging utility
├── assets/                   # Directory for input images
├── outputs/                  # Directory for generated audio files
├── logs/                     # Directory for log files
├── tests/                    # Unit tests for the application
│   ├── __init__.py
│   ├── test_captioning.py    # Tests for captioning
│   ├── test_story.py         # Tests for story generation
│   ├── test_tts.py           # Tests for text-to-speech
├── .streamlit/
│   ├── config.toml           # Streamlit configuration
├── .devcontainer/
│   ├── devcontainer.json     # Dev container configuration
├── requirements.txt          # Python dependencies
├── run_pipeline.py           # CLI pipeline for image-to-audio
├── streamlit_app.py          # Main Streamlit application
├── .gitignore                # Git ignore file
```

## Usage

### Streamlit Interface

1. Upload an image in `.jpg`, `.jpeg`, or `.png` format.
2. Click the "Generate Story" button to process the image.
3. View the generated caption and story.
4. Listen to the story in audio format.

### Command-Line Interface

You can also run the pipeline via the command line:

```bash
python run_pipeline.py <image_filename>
```

Replace `<image_filename>` with the name of the image file in the `assets/` directory.

## Models Used

- **Image Captioning**: `ydshieh/vit-gpt2-coco-en` (Vision-Encoder-Decoder model)
- **Story Generation**: `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (Language model)
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

## Logging

Logs are stored in the `logs/` directory. The application logs both to the console and to a file named `pipeline.log`.

<!-- 
## Testing

Unit tests are located in the `tests/` directory. To run the tests:

```bash
pytest tests/
```
-->
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [Google Text-to-Speech](https://pypi.org/project/gTTS/)