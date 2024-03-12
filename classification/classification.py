import re
import joblib
import numpy as np

model = joblib.load('lr_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def predict_command_with_threshold(input_text, threshold=0.35):
    preprocessed_text = normalize_arabic_characters(input_text)
    text_vector = vectorizer.transform([preprocessed_text])
    probabilities = model.predict_proba(text_vector)[0]
    max_prob = np.max(probabilities)

    if max_prob < threshold:
        return 'error'
    else:
        prediction = np.argmax(probabilities)
        predicted_command = label_encoder.inverse_transform([prediction])[0]
        return predicted_command


def normalize_arabic_characters(text):
    # Normalize Alif forms (أ, إ, آ, ى) to ا
    text = re.sub("[أإآى]", "ا", text)

    # Normalize the two forms of Hamza (ء) either on a carrier or alone
    text = re.sub("[ؤئ]", "ء", text)

    # Normalize different forms of Ya (ي and ى) to ي
    text = re.sub("ى", "ي", text)

    # Normalize different forms of Taa Marbuta (ة) to ه
    text = re.sub("ة", "ه", text)

    # Normalize Waw with Hamza above (ؤ) to و
    text = re.sub("ؤ", "و", text)

    # Remove diacritics (tashkeel)
    text = re.sub("[ًَُ]", "", text)

    # Delete 'ال' at the start of any word in the string.
    # We use a lookahead assertion (?=\S) to ensure 'ال' is directly followed by a non-whitespace character,
    # which helps in identifying it's at the start of a word.
    text = re.sub(r"\bال(?=\S)", "", text)

    return text


def classify(input_text):
    predicted_command = predict_command_with_threshold(input_text)
    return predicted_command
