from dotenv import load_dotenv
import streamlit as st
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Function to get response
def get_response(question):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content


# Streamlit UI
st.set_page_config(page_title="Q&A Demo")

st.header("Groq AI Application")

input_text = st.text_input("Input:", key="input")

submit = st.button("submit")

if submit:

    if input_text.strip() == "":
        st.warning("Please enter a question")

    else:

        try:

            response = get_response(input_text)

            st.subheader("The Response is")

            st.write(response)

        except Exception as e:

            st.error(f"Error: {e}")