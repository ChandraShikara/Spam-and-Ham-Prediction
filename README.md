# Spam and Ham Message Detection

This project provides a robust solution for classifying short text messages (SMS) as either Spam (unsolicited, unwanted) or Ham (legitimate, desired). The application uses a hybrid approach, combining a rule-based system for immediate detection with a powerful machine learning model for nuanced classification.

🌟 Project Overview

The primary goal is to build a highly accurate and efficient message filter. Since false positives (flagging a "Ham" message as "Spam") are extremely damaging to user experience, the system is optimized for high Precision while maintaining strong overall Accuracy.

Key Technology: Hybrid Classifier leveraging Term Frequency-Inverse Document Frequency (TF-IDF) and Support Vector Classification (SVC).

🛠️ Technical Details

Data Preprocessing & Feature Engineering

Data Source: spam.csv (a labeled SMS text message corpus).

Cleaning: Messages are normalized by converting text to lowercase and removing stop words and punctuation.

Vectorization (TF-IDF): Text data is converted into a numerical format using the TF-IDF method.

TF-IDF assigns a weight to each word, emphasizing words that are frequent in a specific message but rare across the entire dataset (e.g., "claim," "prize" in spam messages). 

Model Architecture: Hybrid SVC

The final prediction system utilizes a two-step hybrid approach for speed and accuracy, as implemented in app.py:

Rule-Based Check: The message is first scanned for a predefined list of high-confidence spam keywords (e.g., "win," "free," "claim," "prize"). If a match is found, the message is immediately labeled as Spam.

Machine Learning Classifier (SVC): If the message does not contain immediate keywords, it is passed to the trained Support Vector Classifier (SVC) model.

SVC is an effective model for high-dimensional classification tasks like this, finding the optimal boundary (hyperplane) to separate the Spam and Ham message vectors. 


Accuracy : > 98.35%

Support Vector Classifier (SVC)

📁 Repository Contents

File & Description

Spam and Ham project.ipynb : The Jupyter Notebook containing the full code for data cleaning, TF-IDF transformation, SVC model training, evaluation, and testing.

spam.csv : The raw dataset used for training and testing.

vectorizer.pkl : The serialized TF-IDF Vectorizer object. Essential for transforming new, unseen messages into the numerical format the model expects.

spam_model.pkl : The trained SVC model object, saved using pickle. This is loaded by the web app for inference.

app.py : The Streamlit Python script that deploys the model as an interactive web application.

requirements.txt : List of all Python dependencies needed to run the project.

🚀 Getting Started

Prerequisites

You will need Python and the libraries listed in requirements.txt. Key dependencies include streamlit, scikit-learn, pandas, and pickle.

# Install all required libraries
pip install -r requirements.txt


Running the Web Application

The project is designed to be run as an interactive web app using Streamlit:

# Navigate to the directory containing app.py
streamlit run app.py


This will launch a local server and open the Spam and Ham Message Detector in your web browser, allowing you to enter messages and see real-time predictions.
