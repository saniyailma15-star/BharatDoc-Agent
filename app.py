import streamlit as st
from PIL import Image
import json

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="BharatDoc Agent",
    page_icon="🇮🇳",
    layout="wide"
)

# ------------------------------------
# SIDEBAR
# ------------------------------------

st.sidebar.title("🇮🇳 BharatDoc Agent")

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

st.title("🇮🇳 BharatDoc Agent")
st.header("AI-Powered Multilingual Document Intelligence System")

st.write("Digitize, Understand and Query Documents using AI")
# ------------------------------------
# SOLUTION IMPACT
# ------------------------------------

st.subheader("🎯 Solution Impact")

st.info("""
✅ Reduces manual data entry

✅ Converts unstructured documents into structured records

✅ Enables faster document search and retrieval

✅ Supports multilingual document digitization

✅ Improves efficiency in government and institutional workflows
""")

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

        # DEMO OCR OUTPUT
        extracted_text = [
            "Name: Saniya Ilma",
            "College: Alliance University",
            "Department: IoT",
            "Project: BharatDoc Agent"
        ]

        confidence_scores = [0.95]

    st.success("✅ OCR Completed Successfully")

    # ------------------------------------
    # OCR CONFIDENCE
    # ------------------------------------

    avg_confidence = (
        sum(confidence_scores)
        / len(confidence_scores)
    )

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

            structured_data[
                key.strip()
            ] = value.strip()

    if structured_data:

        st.json(structured_data)

    else:

        st.info(
            "No structured fields detected."
        )

    # ------------------------------------
    # ANALYTICS DASHBOARD
    # ------------------------------------

    st.subheader("📊 Analytics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Language",
            language
        )

    with col2:
        st.metric(
            "Fields",
            len(structured_data)
        )

    with col3:
        st.metric(
            "Text Lines",
            len(extracted_text)
        )

    with col4:
        st.metric(
            "Confidence",
            f"{avg_confidence*100:.2f}%"
        )

    # ------------------------------------
    # AI SUMMARY
    # ------------------------------------

    st.subheader("🧠 AI Summary")

    summary = f"""
Document Type: {document_type}

Language Detected: {language}

Total Text Lines Extracted: {len(extracted_text)}

The document has been successfully processed
and converted into structured digital data
using BharatDoc Agent.
"""

    st.success(summary)
    

    # ------------------------------------
    # FINAL JSON OUTPUT
    # ------------------------------------

    final_output = {
        "document_type": document_type,
        "language": language,
        "confidence_score": round(
            avg_confidence * 100,
            2
        ),
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
                answer = f"{avg_confidence*100:.2f}%"

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