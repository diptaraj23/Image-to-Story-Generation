import streamlit as st
from app.captioning import generate_caption
from app.storytelling import generate_story
from app.tts import speak_story
import tempfile
from PIL import Image

st.set_page_config(page_title="GenAI Storyteller", layout="centered")

st.title("📸🧠 GenAI Storyteller")
st.markdown("Upload an image, get a caption, a story, and hear it spoken aloud!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Process the pipeline on button click
    if st.button("Generate Story"):
        with st.spinner("Generating caption..."):
            # Save uploaded image to a temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                image.save(tmp.name)
                caption = generate_caption(tmp.name)

        st.success("Caption Generated!")
        st.write(f"**Caption**: {caption}")

        with st.spinner("Generating story..."):
            story = generate_story(caption)

        st.success("Story Generated!")
        st.text_area("📖 Story", story, height=250)

        with st.spinner("Generating audio..."):
            audio_path = speak_story(story)

        st.success("Done! Here's the story in audio:")
        audio_file = open(audio_path, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
