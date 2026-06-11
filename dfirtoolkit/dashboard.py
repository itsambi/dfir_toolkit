import streamlit as st

st.set_page_config(
    page_title="DFIR AI Investigation Suite",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ DFIR AI Investigation Suite")

st.markdown(
    """
    ### Intelligent Digital Forensics & Incident Response Platform

    Analyze suspicious files, investigate evidence,
    reconstruct timelines, and generate AI-powered
    incident reports.
    """
)

uploaded_file = st.file_uploader(
    "Upload Suspicious File",
    type=None
)

if uploaded_file:
    st.success(
        f"File Uploaded: {uploaded_file.name}"
    )