import streamlit as st
import gradio_client as grc #0.2.5

st.write(grc.__version__)
client = grc.Client("https://whalb-gpt4all.hf.space/")

st.title("Using free Huggingface models")
st.info("You can almost any huggingface models for development")

prompt = st.text_input('Enter your request here !!!')

if prompt:
    result = client.predict(prompt,fn_index=2)
    st.write(result)