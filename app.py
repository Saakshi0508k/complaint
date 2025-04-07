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
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Draft Complaint with Gemini
    with st.spinner("Generating complaint draft..."):
        prompt = (
    "You are a citizen reporting a public issue through a formal complaint."
    " The image provided shows a Foot Over Bridge (FOB) that is either degraded, broken,"
    " misused by the public (like loitering or encroachment), or poorly maintained."
    " Draft a complaint letter that includes the location if visible, describes the condition,"
    " the risks it poses to pedestrians (especially elderly or disabled), and request authorities"
    " to take prompt action to repair or manage the situation."
    )

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
