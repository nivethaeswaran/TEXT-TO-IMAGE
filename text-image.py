import streamlit as st
import requests
import io
from PIL import Image

# Use Markdown syntax to set the title color to red
st.markdown(
    "<h1 style='color: red;'>Streamlit Application Text to Image</h1>",
    unsafe_allow_html=True,
)

# Create a text input box for the image name
image_name = st.text_input("Enter the Image Name")

# Create a button to trigger image generation
generate_button = st.button("Generate Image")

# Check if the user has entered a name and clicked the button
if image_name and generate_button:
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query({
        "inputs": "Lion riding a bike",  # Use the user-entered text as input
    })

    # Check if image generation was successful
    if image_bytes:
        # Convert the image bytes to a PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        # Display the generated image
        st.image(image, caption=f"Generated Image: {image_name}", use_column_width=True)
    else:
        # Display an error message if image generation failed
        st.error("Image generation failed. Please try again with a different input.")
elif generate_button:
    # Display a message if the user clicked the button without entering a name
    st.warning("Please enter an image name before generating.")