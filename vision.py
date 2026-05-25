from dotenv import load_dotenv
import streamlit as st
import os
import base64
from groq import Groq

# Load env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.set_page_config(page_title="Groq Image App")

st.header("Groq AI Application")

input_text = st.text_input("Enter prompt:")
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

submit = st.button("Submit")


def encode_image(file):
    return base64.b64encode(file.read()).decode("utf-8")


def get_response(prompt, file):

    base64_image = encode_image(file)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt if prompt else "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )

    return response.choices[0].message.content


if submit:

    if uploaded_file is not None:

        result = get_response(input_text, uploaded_file)

        st.subheader("Response")
        st.write(result)

    else:
        st.warning("Please upload an image")