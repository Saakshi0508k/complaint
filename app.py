import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Setup Gemini API
genai.configure(api_key="AIzaSyCFA_ppwTGV1AQp5J7oeqJCis2cVzvIM3s")
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("📷 Complaint Registration Portal")

# Image Upload
uploaded_file = st.file_uploader("Upload a photo related to your complaint", type=["jpg", "png", "jpeg"])
complaint_draft = ""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Draft Complaint with Gemini
    with st.spinner("Generating complaint draft..."):
        prompt = "Generate a formal complaint based on the image provided. Assume it's related to a public issue."
        response = model.generate_content([prompt, image])
        complaint_draft = response.text.strip()
    
    # Show and Edit Complaint
    st.subheader("📝 Complaint Draft")
    edited_complaint = st.text_area("You can edit the complaint below:", value=complaint_draft, height=250)

    # Submit
    if st.button("Submit Complaint"):
        st.success("✅ Complaint submitted successfully!")
        # You can store this in a DB, send it via email, etc.
        st.write("**Final Submitted Complaint:**")
        st.write(edited_complaint)
