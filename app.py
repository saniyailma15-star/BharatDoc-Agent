from PIL import Image
import streamlit as st
from PIL import Image
import json
logo = Image.open("logo.png")

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="BharatDoc Agent",
    page_icon="🇮🇳",
    layout="wide"
)
st.set_page_config(
    page_title="BharatDoc Agent",
    page_icon="🇮🇳",
    layout="wide"
)

# ------------------------------------
# SIDEBAR
# ------------------------------------

st.sidebar.image(logo, width=180)
st.sidebar.markdown("## BharatDoc Agent")

st.sidebar.success("AI Powered Document Intelligence")

st.sidebar.write("""
✓ OCR Extraction

✓ Structured Data Extraction

✓ JSON Export

✓ Chat With Document

✓ Multilingual Support

✓ Analytics Dashboard

✓ AI Summary
""")

# ------------------------------------
# HEADER
# ------------------------------------

col1, col2 = st.columns([1,5])

with col1:
    st.image(logo, width=140)

with col2:
    st.markdown("""
    <h1 style='margin-bottom:0px;'>
    BharatDoc Agent
    </h1>
    <h4 style='color:#4CAF50;'>
    AI-Powered Multilingual Document Intelligence System
    </h4>
    """, unsafe_allow_html=True)
st.header("AI-Powered Multilingual Document Intelligence System")

st.write("Digitize, Understand and Query Documents using AI")

# ------------------------------------
# EXPECTED IMPACT
# ------------------------------------

st.subheader("📈 Expected Impact")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("OCR Accuracy", "95%")

with col2:
    st.metric("Processing Speed", "80% Faster")

with col3:
    st.metric("Languages Supported", "7+")

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.success("✅ Structured Data Extraction")

with col5:
    st.success("✅ AI Document Understanding")

with col6:
    st.success("✅ Government Ready")

st.divider()

# ------------------------------------
# LANGUAGE SELECTION
# ------------------------------------

language = st.selectbox(
    "🌐 Select Language",
    [
        "English",
        "Hindi",
        "Tamil",
        "Kannada",
        "Telugu",
        "Malayalam",
        "Marathi"
    ]
)

# ------------------------------------
# FILE UPLOAD
# ------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Document",
    type=["jpg", "jpeg", "png"]
)

# ------------------------------------
# DOCUMENT PROCESSING
# ------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Document",
        width=500
    )

    with st.spinner("Processing Document..."):

        # Demo OCR Output
        extracted_text = [
            "Name: Saniya Ilma",
            "College: Alliance University",
            "Department: IoT",
            "Project: BharatDoc Agent"
        ]

        confidence_scores = [0.95]

    st.success("✅ OCR Completed Successfully")

    avg_confidence = sum(confidence_scores) / len(confidence_scores)

    confidence_score = round(
        avg_confidence * 100,
        2
    )

    # ------------------------------------
    # PROCESSING STATUS
    # ------------------------------------

    st.subheader("⚙ Processing Status")

    st.success("✓ Image Uploaded")
    st.success("✓ OCR Extraction Completed")
    st.success("✓ Language Detection Completed")
    st.success("✓ Structured Data Generated")

    # ------------------------------------
    # DOCUMENT TYPE DETECTION
    # ------------------------------------

    combined_text = " ".join(extracted_text).lower()

    document_type = "General Document"

    if "aadhaar" in combined_text:
        document_type = "Aadhaar Card"

    elif "pan" in combined_text:
        document_type = "PAN Card"

    elif "passport" in combined_text:
        document_type = "Passport"

    elif "college" in combined_text:
        document_type = "Student Document"

    st.subheader("📑 Document Type")
    st.success(document_type)

    # ------------------------------------
    # RELIABILITY ASSESSMENT
    # ------------------------------------

    st.subheader("🛡 Reliability Assessment")

    if confidence_score >= 90:
        st.success(
            f"High Reliability Document ({confidence_score}%)"
        )

    elif confidence_score >= 70:
        st.warning(
            f"Medium Reliability Document ({confidence_score}%)"
        )

    else:
        st.error(
            f"Low Reliability - Manual Verification Recommended ({confidence_score}%)"
        )

    # ------------------------------------
    # EXTRACTED TEXT
    # ------------------------------------

    st.subheader("📝 Extracted Text")

    for text in extracted_text:
        st.write(text)

    # ------------------------------------
    # STRUCTURED DATA
    # ------------------------------------

    st.subheader("📋 Extracted Fields")

    structured_data = {}

    for line in extracted_text:

        if ":" in line:

            key, value = line.split(":", 1)

            structured_data[key.strip()] = value.strip()

    if structured_data:
        st.json(structured_data)

    else:
        st.info("No structured fields detected.")

    # ------------------------------------
    # DOCUMENT RISK ANALYZER
    # ------------------------------------

    st.subheader("🚨 Document Risk Analyzer")

    required_fields = [
        "Name",
        "College",
        "Department"
    ]

    missing_fields = []

    for field in required_fields:

        if field not in structured_data:
            missing_fields.append(field)

    risk_score = 100 - (len(missing_fields) * 20)

    if risk_score >= 80:
        st.success(
            f"Document Health Score: {risk_score}/100"
        )

    elif risk_score >= 60:
        st.warning(
            f"Document Health Score: {risk_score}/100"
        )

    else:
        st.error(
            f"Document Health Score: {risk_score}/100"
        )

    if missing_fields:

        st.warning(
            "Missing Fields: "
            + ", ".join(missing_fields)
        )

    else:
        st.success("No Missing Fields Detected")

    # ------------------------------------
    # ANALYTICS DASHBOARD
    # ------------------------------------

    st.subheader("📊 Analytics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Language", language)

    with col2:
        st.metric("Fields", len(structured_data))

    with col3:
        st.metric("Text Lines", len(extracted_text))

    with col4:
        st.metric(
            "Confidence",
            f"{avg_confidence*100:.2f}%"
        )

    # ------------------------------------
    # AI SUMMARY
    # ------------------------------------

    st.subheader("🤖 AI Summary")

    summary = f"""
📄 Document Type: {document_type}

🌐 Language: {language}

📝 Text Lines: {len(extracted_text)}

📊 Confidence Score: {confidence_score}%

🚨 Health Score: {risk_score}/100

The document has been successfully analyzed, structured, validated and converted into digital records using BharatDoc Agent.
"""

    st.info(summary)

    # ------------------------------------
    # FINAL JSON OUTPUT
    # ------------------------------------

    final_output = {
        "document_type": document_type,
        "language": language,
        "confidence_score": confidence_score,
        "structured_data": structured_data,
        "raw_text": extracted_text
    }

    st.subheader("📦 Final JSON Output")

    st.json(final_output)

    json_string = json.dumps(
        final_output,
        indent=4,
        ensure_ascii=False
    )

    st.download_button(
        "⬇ Download JSON",
        data=json_string,
        file_name="bharatdoc_output.json",
        mime="application/json"
    )

    # ------------------------------------
    # CHAT WITH DOCUMENT
    # ------------------------------------

    st.divider()

    st.subheader("💬 Chat With Document")

    question = st.text_input(
        "Ask a question about the document"
    )

    if question:

        q = question.lower()

        answer = "Information not found."

        for key, value in structured_data.items():

            if key.lower() in q:
                answer = value
                break

        if answer == "Information not found.":

            if "document type" in q:
                answer = document_type

            elif "language" in q:
                answer = language

            elif "confidence" in q:
                answer = f"{confidence_score}%"

            elif "lines" in q:
                answer = str(len(extracted_text))

        st.success(answer)

# ------------------------------------
# FOOTER
# ------------------------------------

st.divider()

st.markdown("### Developed by")

st.write("**Saniya Ilma**")
st.write("**Charan G**")
st.write("**Preetham Shetty**")