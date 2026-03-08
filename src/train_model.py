import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load training data
data = pd.read_csv("data/training_text.csv")

# Separate text and labels
texts = data["text"]
labels = data["sdg"]

# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Create machine learning model
model = LogisticRegression()

# Train model
model.fit(X, labels)

# Save trained model
pickle.dump(model, open("models/sdg_model.pkl", "wb"))

# Save vectorizer
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("Model trained and saved successfully")