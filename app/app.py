from pathlib import Path
import sys
import time
import re

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.predictor import predict_email

st.set_page_config(
    page_title="AI-Driven Phishing Email Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:

    st.title("🛡️ Project Information")

    st.markdown("---")

    st.subheader("🤖 Model")
    st.write("Neural Network (MLP)")

    st.subheader("📊 Accuracy")
    st.success("96.62%")

    st.subheader("📂 Dataset")
    st.write("18,650 Emails")

    st.subheader("🧠 Feature Engineering")
    st.write("TF-IDF (5000 Features)")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.write("""
- Python
- NLP
- NLTK
- Scikit-Learn
- Streamlit
- Pandas
- Joblib
""")

    st.markdown("---")

    st.info(
        "This AI application predicts whether an email is Safe or Phishing using Machine Learning."
    )

st.title("🛡️ AI-Driven Phishing Email Detection")

st.markdown("""
Detect phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**.

Paste an email below and click **Detect Email**.
""")

st.markdown("---")

email = st.text_area(
    "📧 Paste Email Here",
    height=300,
    placeholder="Paste your email content here..."
)

detect = st.button(
    "🔍 Detect Email",
    use_container_width=True
)

if detect:

    if email.strip() == "":
        st.warning("⚠ Please enter an email.")

    else:

        start = time.time()

        prediction, confidence = predict_email(email)

        end = time.time()

        processing_time = end - start

        st.markdown("---")

        if prediction == 1:
            st.error("## 🚨 PHISHING EMAIL DETECTED")
        else:
            st.success("## ✅ SAFE EMAIL")

        st.subheader("Confidence")

        st.progress(float(confidence))

        st.write(f"**Confidence Score:** {confidence*100:.2f}%")

        st.write(f"**Processing Time:** {processing_time:.3f} seconds")

        st.markdown("---")

        st.subheader("📊 Email Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Characters", len(email))
            st.metric("Words", len(email.split()))

        with col2:
            urls = len(re.findall(r"http\S+|www\S+", email))
            emails = len(re.findall(r"\S+@\S+", email))

            st.metric("URLs", urls)
            st.metric("Email IDs", emails)

        with col3:
            numbers = len(re.findall(r"\d", email))
            lines = len(email.split("\n"))

            st.metric("Numbers", numbers)
            st.metric("Lines", lines)

        st.markdown("---")

        st.subheader("🛡 Security Recommendations")

        if prediction == 1:

            st.warning("""
✔ Do NOT click suspicious links.

✔ Verify the sender's email address.

✔ Never share passwords or OTPs.

✔ Report suspicious emails to your IT team.

✔ Delete phishing emails immediately.
""")

        else:

            st.success("""
✔ Email appears safe.

✔ Always verify unknown senders.

✔ Keep antivirus software updated.

✔ Avoid downloading unexpected attachments.

✔ Stay alert for future phishing attempts.
""")

st.markdown("---")

st.caption(
    "Developed by Harshvardhan Natu | AI-Driven Phishing Email Detection using NLP & Machine Learning"
)