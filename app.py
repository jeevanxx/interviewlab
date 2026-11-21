import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="InterviewLab — AI Mock Interview", page_icon="🎤", layout="wide")

# Hide Streamlit's default chrome so the app fills the page
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1400, scrolling=True)
