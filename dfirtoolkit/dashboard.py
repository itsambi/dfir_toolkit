from hashing.file_hash import calculate_hashes
from metadata.file_metadata import get_file_metadata
from analysis.suspicious_detector import analyze_file
from risk_engine.risk_scoring import calculate_risk
from ioc_detection.ioc_detector import detect_iocs

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

    analyze = st.button(
        "🔍 Analyze Evidence"
    )

    if analyze:

        # Save uploaded file locally
        with open(
            uploaded_file.name,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        file_path = uploaded_file.name

        # Run DFIR Analysis
        metadata_results = get_file_metadata(
            file_path
        )

        risk_results = calculate_risk(
            file_path
        )

        ioc_results = detect_iocs(
            file_path
        )

        # Metrics Row
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Risk Score",
                risk_results["Risk Score"]
            )

        with col2:
            st.metric(
                "IOC Indicators",
                len(ioc_results)
            )

        with col3:
            st.metric(
                "Timeline Events",
                "12"
            )

        with col4:
            st.metric(
                "Evidence Sources",
                "3"
            )

        st.divider()

        # Threat Assessment
        st.subheader("Threat Assessment")

        risk_level = risk_results["Risk Level"]

        if risk_level == "HIGH":

            st.error(
                "HIGH RISK INCIDENT DETECTED"
            )

        elif risk_level == "MEDIUM":

            st.warning(
                "MEDIUM RISK INCIDENT DETECTED"
            )

        else:

            st.success(
                "LOW RISK INCIDENT DETECTED"
            )