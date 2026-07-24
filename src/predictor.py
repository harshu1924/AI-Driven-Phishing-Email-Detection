from pathlib import Path
import joblib

from src.preprocessing import preprocess_text

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "phishing_detector.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_email(email_text):
    """
    Predict whether an email is Safe or Phishing.
    Returns:
        prediction (0 or 1)
        confidence (0-1)
    """

    processed_text = preprocess_text(email_text)

    vector = vectorizer.transform([processed_text])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = max(probability)

    return prediction, confidence