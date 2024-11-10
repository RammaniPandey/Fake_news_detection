from flask import Flask, render_template, request
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))  # Assuming you saved the vectorizer as well

# Preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Removing URLs
    text = re.sub(r'<.*?>', '', text)  # Removing HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Removing punctuation
    text = re.sub(r'\d', '', text)  # Removing numbers
    text = re.sub(r'\n', ' ', text)  # Removing newlines
    return text

# News classification function
def classify_news(text):
    processed_text = wordopt(text)
    vectorized_text = vectorizer.transform([processed_text])  # Vectorize the cleaned text
    prediction = model.predict(vectorized_text)
    
    # Check prediction value to determine if it's fake or real
    if prediction[0] == 1:
        return "Fake News"
    elif prediction[0] == 0:
        return "Real News"
    else:
        return "Unable to Classify"  # In case the model returns an unexpected value

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_article = request.form['news_article']
        prediction = classify_news(news_article)
        return render_template('index.html', prediction=prediction, news_article=news_article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
