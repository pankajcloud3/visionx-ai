# from dotenv import load_dotenv
# import streamlit as st
# import os
# from google import genai

# # Load environment variables
# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# # Create Gemini client
# client = genai.Client(api_key=api_key)

# # Function to get response
# def get_response(question):

#     response = client.models.generate_content(
#         model="gemini-2.0-flash-lite",
#         contents=question
#     )

#     return response.text

# # Initialize Streamlit app
# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini Application")

# input_text = st.text_input("Input:", key="input")

# submit = st.button("submit")

# if submit and input_text:

#     try:

#         response = get_response(input_text)

#         st.subheader("The Response is")

#         st.write(response)

#     except Exception as e:

#         st.error(f"Error: {e}")
