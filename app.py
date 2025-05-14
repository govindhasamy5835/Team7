import streamlit as st
from PIL import Image
from model_utils import predict_skin_cancer
from chatbot import get_bot_response

st.set_page_config(page_title="Skin Cancer Detector & Chatbot", layout="centered")

st.title("🧴 Skin Cancer Prediction with Chatbot")

st.sidebar.title("💬 Chatbot Assistant")

user_query = st.sidebar.text_input("You:", key="user_input")
if user_query:
    bot_reply = get_bot_response(user_query)
    st.sidebar.markdown(f"**Bot:** {bot_reply}")

uploaded_image = st.file_uploader("Upload a skin lesion image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    with st.spinner("Predicting..."):
        result = predict_skin_cancer(image)
    st.success(f"Prediction: **{result}**")

    st.sidebar.markdown(f"**Bot:** {get_bot_response(result.lower())}")