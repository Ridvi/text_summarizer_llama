import streamlit as st
import requests
import re

st.title("LLaMA Text Summarizer")

user_input = st.text_area("Enter the text you want to summarize:")

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    data={"text": user_input},
                    timeout=30
                )
                summary = response.text
                summary = re.sub(r'\n+', '', summary)
                if summary:
                    st.subheader("Summary:")
                    st.write(summary)
                else:
                    st.warning("The backend returned an empty summary.")


            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to backend: {e}")
