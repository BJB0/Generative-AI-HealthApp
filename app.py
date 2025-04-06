import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")  # <- define model here


# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(prompt, image_bytes):
    response = model.generate_content([
        {"text": prompt},
        {"inline_data": {
            "mime_type": "image/png",  # or image/jpeg depending on the input
            "data": image_bytes
        }}
    ])
    return response.text


# Function to extract bytes from uploaded file
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return uploaded_file.getvalue()  # returns image as bytes
    else:
        raise FileNotFoundError("No file uploaded")


# Streamlit App UI
st.set_page_config(page_title="Calories Advisor APP")

st.header("Calories Advisor APP 🍱")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the total calories")

input_prompt = """
You are a world-class nutritionist and AI food analyst. Analyze the food shown in the image and provide the following details in a clean and point-wise format:

1. Identify and list **each food item** in the image.
2. Mention the **approximate serving size** and **estimated calories** for each item.
3. Present the results clearly like this:

   🔸 Item Name (Serving Size) - XYZ calories

4. After listing all items, mention the:

   ✅ **Total Estimated Calories**  
   ⚖️ **Health Analysis**:
     - Is this meal considered healthy or unhealthy?
     - Brief reasoning based on nutritional content (e.g., fried, sugary, balanced, high protein, etc.)
     - Mention if it is suitable for daily consumption or occasional treat.

5. If the meal is unhealthy, give 1-2 quick suggestions to make it healthier (e.g., reduce portion, swap ingredients).

If the image is unclear or some items can't be confidently identified, please mention that too.
Be informative, concise, and neatly formatted using bullet points and symbols.
"""



# Handle Submit
if submit:
    image_bytes = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_bytes)
    st.header("The Response is:")
    st.write(response)
