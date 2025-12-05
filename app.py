import streamlit as st
import pickle

# Load the trained model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Spam keywords
spam_keywords = [
    "win", "prize", "free", "offer", "deal", "loan", "credit",
    "cash", "buy 1 get 1", "limited time", "apply now", "click here", "reward"
]

# Hybrid prediction function
def predict_hybrid(msg):
    msg_lower = msg.lower()
    for keyword in spam_keywords:
        if keyword in msg_lower:
            return "spam"
    msg_vec = vectorizer.transform([msg])
    return model.predict(msg_vec)[0]

# Streamlit UI
st.title("Spam and Ham Message Detector")
st.write("Enter your message below to check if it is spam or ham:")

user_input = st.text_area("Message here")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to predict.")
    else:
        prediction = predict_hybrid(user_input)
        if prediction == "spam":
            st.error(f"The message is: {prediction.upper()}")
        else:
            st.success(f"The message is: {prediction.upper()}")
