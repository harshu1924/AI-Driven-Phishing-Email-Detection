import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download resources (only first time)
# Download NLTK resources for Streamlit Cloud

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


def clean_text(text):
    """Basic text cleaning"""

    text = str(text).lower()

    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\d+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_text(text):
    """Tokenization + Stopword Removal + Stemming"""

    text = clean_text(text)

    words = word_tokenize(text)

    processed = []

    for word in words:

        if word.isalpha():

            if word not in stop_words:

                processed.append(stemmer.stem(word))

    return " ".join(processed)