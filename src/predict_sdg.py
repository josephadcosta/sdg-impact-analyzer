import pickle

# Load model
model = pickle.load(open("models/sdg_model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Example text
text = "solar irrigation for rural farmers"

X = vectorizer.transform([text])

prediction = model.predict(X)

print("Predicted SDG:", prediction[0])